from matplotlib import colors
import pandas as pd
import matplotlib.pyplot as plt

path_data = "fields_separados.xlsx"
df = pd.read_excel(path_data)

# print(df.prediction) # Prospectivo Retrospectivo
def pie_chart(perspective, perspective_name, number_categories=-1):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    for index_loop, i in enumerate(perspective):
        df_chart = df.loc[df.prediction == i]
        a = df_chart['Field'].value_counts()
        
        # Rest category
        if (number_categories==-1):
            number_categories=len(a) - 1
        tresh = a[number_categories] + 0.001
        count = a[a > tresh]
        count['REST'] = a[a <= tresh].sum()

        # Black and white scale
        number_categories+=1
        small_fraction_color=0.55/number_categories
        start_point= 0.1
        colors_list=[]
        for position, value in enumerate(range(number_categories)):
            colors_list.append((0,0,0,start_point+small_fraction_color*position))

        index = count.index
        if index_loop ==0:
            ax1.pie(count, labels=index, startangle=90, autopct='%.1f%%', colors = colors_list)
            ax1.set_title("Retrospective")
        else:
            ax2.pie(count, labels=index, startangle=90, autopct='%.1f%%', colors = colors_list)
            ax2.set_title("Prospective")
    # ax.set_title(perspective_name)
    plt.show()

number_fields = 8
pie_chart(["Retrospectivo", "Prospectivo"], "Frequency of fields of study in Retrospective articles", number_fields)
# pie_chart(, "Frequency of fields of study in Prospective articles", number_fields)

