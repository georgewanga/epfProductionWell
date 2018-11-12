import csv
import os.path
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.conf import settings
from mercuryManometer.models import MercuryManometerTable


def index_view(request):
    fields = (
        'Time', 'Differential_Pressure', 'Weir_Height', 'Upstream_Pressure', 'Steam_flow_rate',
        'Corr_Water_flow','Mass_Flow_rate', 'Stream_enthalpy', 'combined_enthalpy', 'Whp')
    
    if request.method == 'POST' and request.FILES['mercuryManometer']:
        my_file = request.FILES['mercuryManometer']
        file_name = my_file.name
        title = 'Mercury Manometer'

        save_url = (settings.MEDIA_ROOT + 'mercuryManometer/').replace('\\','/')
        file_url = (save_url + file_name).replace('\\', '/') 

        if file_name.endswith('.csv'):
            if os.path.isfile(file_url):
                information = 'DUPLICATE! A file with the name "'+file_name+'" already savd before. Please consider renamming your file and try again.'
            else:
                FileSystemStorage(location=save_url).save(file_name, my_file)
                information = file_name+' successfully uploaded'

                with open(file_url, "r") as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        csv_dict = dict(zip(fields, row))
                        MercuryManometerTable(**csv_dict).save()
                    information = title+' table data successfully updated'
        else:
            information = 'NON CSV FILE! The file "'+file_name+'" is not a csv file. Consider using .csv files only.'
        context = {
            'information': information,
            'title': title,
        }
        
        content_type = None
        return render(request, 'base/success.html', context, content_type)
    else:
        all_data = MercuryManometerTable.objects.all()
        context = {
            'all_data': all_data,
            'fields': fields,
            'title': 'Mercury Manometer',
        }
        content_type = None
        return render(request, 'mercuryManometer/index.html', context, content_type)
