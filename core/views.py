from django.shortcuts import render
from .utils import exercicio1, exercicio2,exercicio3
# Create your views here.
from django.views.generic import TemplateView


class MenuView(TemplateView):
    template_name = 'menu.html'


class OneView(TemplateView):
    template_name = 'Exercicio1.html'

    def get(self, request, *args, **kwargs):
        (Room1, Room2, Room3, Room4) = exercicio1()
        max1 = Room1.max()
        max2 = Room2.max()
        max3 = Room3.max()
        max4 = Room4.max()

        Room1 = Room1.to_json()
        Room2 = Room2.to_json()
        Room3 = Room3.to_json()
        Room4 = Room4.to_json()

        context = {"Room1": Room1, "Room2": Room2, "Room3": Room3, "Room4": Room4,
                   "max1": max1, "max2": max2, "max3": max3, "max4": max4}

        return render(request, self.template_name, context)


class TwoView(TemplateView):
    template_name = 'Exercicio2.html'

    def get(self, request, *args, **kwargs):
        correlation_matrix, Room1, Room2, Room3, Room4 = exercicio2()

        Room1 = Room1.Router1.to_json(orient='values')
        Room2 = Room2.to_json()
        Room3 = Room3.to_json()
        Room4 = Room4.to_json()

        context = {"table_values": correlation_matrix.values,
                   "Room1": Room1, "Room2": Room2, "Room3": Room3, "Room4": Room4}

        return render(request, self.template_name, context)


class ThreeView(TemplateView):
    template_name = 'Exercicio3.html'
    #TODO: colocar legenda certa

    def get(self, request, *args, **kwargs):
        general_mean, mean1, mean2, mean3, mean4 = exercicio3()
        a = general_mean
        b = mean1
        c = mean2
        d = mean3
        e = mean4

        general_mean = general_mean.to_json()
        mean1 = mean1.to_json()
        mean2 = mean2.to_json()
        mean3 = mean3.to_json()
        mean4 = mean4.to_json()

        context = dict(mean1=mean1, mean2=mean2, mean3=mean3, mean4=mean4, general_mean=general_mean, a=a, b=b, c=c,
                       d=d, e=e)

        return render(request, self.template_name, context)

class Four(TemplateView):
    template_name = "Exercicio4.html"
