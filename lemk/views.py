# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
import random
from django.core.mail import send_mail
from datetime import datetime
from django import forms
from django.views.generic import CreateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout
from crispy_forms.bootstrap import FormActions
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from myproject.settings import EMAIL_HOST_USER, ADMIN_EMAIL

# Create your views here.

#Russian Locale
class ContactFormRus(forms.Form):
	"""docstring for ContactFormRus"""

	def __init__(self, *args, **kwargs):
		#call original initializator
		super(ContactFormRus, self).__init__(*args, **kwargs)

		#this helper object allows us to us to customize form
		self.helper =FormHelper()

		#form tag attributes
		self.helper.form_class ='form-horizontal'
		self.helper.form_method ='post'
		self.helper.form_action =reverse('home')

		#twitter bootstrap styles
		self.helper.help_text_inline =True
		self.helper.html5_required =True
		self.helper.label_class ='col-sm-2 control label'
		self.helper.field_class ='col-sm-10'


def main_page(request):
	title = u'СООБЩЕНИЕ НА LEMK. Имя: '
	txt = u', тел: '
	from_email = EMAIL_HOST_USER

	if request.method =='POST':
		form = ContactFormRus(request.POST)
		subject = title + request.POST['name'] + txt + request.POST['phone']
		message = request.POST['message']
		try:
			send_mail(subject, message, from_email, [ADMIN_EMAIL])
		except Exception:
			message = u"Возникла ошибка при отправке сообщения"
		else:
			message = u"Сообщение отправлено успешно !"
		return HttpResponseRedirect(
			u'%s?status_message=%s' % (reverse('home'), message))

	return render(request, 'lemk/index.html', {})

