from django.shortcuts import render
import pandas as pd
from django.conf import settings
from sqlalchemy import create_engine 
from .models import data

# def row_color(s):
#     for e in s:
#         if e[0:2]=='CR':
#             return ['background-color: pink']
#         elif e[0:2]=='AP':
#             return ['background-color: yellow']
#         else:
#             return ['background-color: lightgreen']


def transfer(df):
    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']

    database_url = 'mysql://{user}:{password}@localhost/{database_name}'.format(
    user=user,
    password=password,
    database_name=database_name)

    engine = create_engine(database_url, echo=False)
    return (df.to_sql('display_data', con=engine,index=False,if_exists='replace'))



def display(request):
    
    data1={"1": {"id": "1", "order_no": "CR235134","name": "Linda Johnson", "booking_datetime": "2019-07-02 14:29:24","date": "29/10/2019", "amount": "1250","no_of_people": "2"},"2": {"id": "2","order_no": "CR64838","name": "Chris Martin","booking_datetime": "2019-06-07 12:19:14","date": "19/09/2019","amount": "1550", "no_of_people": "5"},"3": {"id": "3","order_no": "AP246153", "name": "Vasu Khare","booking_datetime": "2019-06-22 06:19:54","date": "12/08/2019","amount": "570","no_of_people": "4"},"4": {"id": "4","order_no": "CR237529","name": "Iqbal", "booking_datetime": "2019-07-02 14:29:24","date": "15/10/2019", "amount": "990","no_of_people": "3"},"5": {"id": "5","order_no": "AP765136","name": "Narendra Gandhi","booking_datetime": "2019-07-02 14:29:24","date": "08/11/2019","amount": "2250", "no_of_people": "1"},"6": {"id": "6","order_no": "KL144172", "name": "Donald Obama","booking_datetime": "2019-07-02 14:29:24","date": "09/12/2019","amount": "9250", "no_of_people": "2"},"7": {"id": "7","order_no": "CR753934", "name": "Lana Del Rey","booking_datetime": "2019-07-02 14:29:24","date": "23/10/2019","amount": "50","no_of_people": "1"}}
    df = pd.DataFrame.from_dict(data1,orient='columns')
    df=df.transpose()
    
    transfer(df)
    
    order_by = request.GET.get('order_by', default='id')
    displaydata=data.objects.all().order_by(order_by)
    
    return render(request,'display.html',{'json_data':displaydata})    
    #df=df.style.apply(row_color,subset=['order_no'],axis=1)
    #return render(request,'display.html')