import pandas as pd
import matplotlib.pyplot as plt
# Я использовала библиотеку pandas, чтобы прочитать файл excel, в котором хранится информация
# о кафе и ресторанах в городе Москве
# Далее я отсортировала нужные мне районы и с помощью библиотеки matplotlib и графика, высчитала в каком из перечисленных
# районов больше всего заведений общественного питания.

dataset = pd.read_excel('only_last.xlsx')
dataset = pd.DataFrame(dataset.groupby(['District']).count())
dataset = pd.DataFrame(dataset['City'])
dataset = dataset.rename(columns={'City': 'Count'})
dataset = dataset.reset_index()

District_search = ['Академический',
 'Алексеевский',
 'Алтуфьевский',
 'Арбат',
 'Аэропорт',
 'Бабушкинский',
 'Басманный',
 'Беговой',
 'Бескудниковский',
 'Бибирево',
 'Бирюлево Восточное',
 'Бирюлево Западное',
 'Богородское',
 'Братеево',
 'Бутырский']


dataset = dataset[dataset['District'].isin(District_search)]



name_ = dataset['District'].tolist()
count_ = dataset['Count'].tolist()

plt.barh(name_, count_, label='Кол-во ресторанов',alpha=1.0) #Параметр label позволяет задать название величины для легенды
plt.xlabel('Кол-во ресторанов')
plt.ylabel('Округа')
plt.title('Распределение ресторанов по округам')
plt.legend()
plt.show()
