import csv
import os.path
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.conf import settings
from numericalModeling.models import NumericalModelingTable


def index_view(request):
    fields = ('Date', 'Flow_Rate', 'Totals')
    if request.method == 'POST' and request.FILES['numericalModeling']:
        my_file = request.FILES['numericalModeling']
        file_name = my_file.name
        title = 'Numerical Modeling'

        save_url = (settings.MEDIA_ROOT + 'numericalModeling/').replace('\\','/')
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
                        NumericalModelingTable(**csv_dict).save()
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
        all_data = NumericalModelingTable.objects.all()
        context = {
            'all_data': all_data,
            'fields': fields,
            'title': 'Numerical Modeling',
        }
        content_type = None
        return render(request, 'numericalModeling/index.html', context, content_type)
