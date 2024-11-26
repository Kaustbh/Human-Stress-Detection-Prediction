import csv,io
from django.shortcuts import render
from .forms import Predict_Form
from predict_risk.data_provider import *
from accounts.models import UserProfileInfo, ConcreteUserProfile
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.urls import reverse
from django.contrib import messages

# @login_required(login_url='/')
# def PredictRisk(request,pk):
#     predicted = False
#     predictions={}
#     if request.session.has_key('user_id'):
#         u_id = request.session['user_id']

#     if request.method == 'POST':
#         form = Predict_Form(data=request.POST)
#         profile = get_object_or_404(ConcreteUserProfile, pk=pk)

#         if form.is_valid():
#             features = [[ form.cleaned_data['sr'], form.cleaned_data['rr'], form.cleaned_data['bt'], form.cleaned_data['lm'], form.cleaned_data['blood_ol'],
#             form.cleaned_data['em'], form.cleaned_data['sh'], form.cleaned_data['hr']]]

#             standard_scalar = GetStandardScalarForStress()
#             features = standard_scalar.transform(features)
#             ANNClassifier=GetAllClassifiersForstress()
 
#             # predictions = {'ANN': str(ANNClassifier.predict(features)[0]),}
#             # ann_prediction = ANNClassifier.predict(features)[0]

#             raw_prediction = ANNClassifier.predict(features)[0]
#             ann_prediction = 1 if raw_prediction >= 0.7 else 0

#             pred = form.save(commit=False)
#             pred.num = int(ann_prediction) 
#             # l=[predictions['ANN']]
#             # count=l.count('1')

#             result=False

#             if pred.num==1:
#                 result=True
#             else:
#                 pred.num==0
#             # if count>=2:
#             #     result=True
#             #     pred.num=1
#             # else:
#             #     pred.num=0


#             pred.profile = profile

#             pred.save()
#             predictions = {'ANN': str(ann_prediction)}
#             predicted = True

#             colors={}
 
#             if predictions['ANN']=='0':
#                 colors['ANN']="table-success"
#             else:
#                 colors['ANN']="table-danger"

#     if predicted:
#         return render(request, 'predict.html',
#                       {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions,'result':result,'colors':colors})

#     else:
#         form = Predict_Form()

#         return render(request, 'predict.html',
#                       {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions})

@login_required(login_url='/')
def PredictRisk(request, pk):
    predicted = False  # Initialize as False
    predictions = {}
    colors = {}  # Default color dictionary
    result = False  # Default result status
    
    if request.session.has_key('user_id'):
        u_id = request.session['user_id']

    if request.method == 'POST':
        form = Predict_Form(data=request.POST)
        profile = get_object_or_404(ConcreteUserProfile, pk=pk)

        if form.is_valid():
            # Process the form only if it's valid
            features = [[
                form.cleaned_data['sr'], form.cleaned_data['rr'], form.cleaned_data['bt'],
                form.cleaned_data['lm'], form.cleaned_data['blood_ol'], form.cleaned_data['em'],
                form.cleaned_data['sh'], form.cleaned_data['hr']
            ]]

            # Standardize the features
            standard_scalar = GetStandardScalarForStress()
            features = standard_scalar.transform(features)

            # Load the classifier
            ANNClassifier = GetAllClassifiersForstress()

            # Make predictions
            raw_prediction = ANNClassifier.predict(features)[0]
            ann_prediction = 1 if raw_prediction >= 0.7 else 0

            # Save the prediction
            pred = form.save(commit=False)
            pred.num = int(ann_prediction)
            result = pred.num == 1  # True for stressed, False otherwise
            pred.profile = profile
            pred.save()

            # Update results for rendering
            predictions = {'ANN': str(ann_prediction)}
            colors['ANN'] = "table-danger" if ann_prediction == 1 else "table-success"
            predicted = True

        else:
            # If form is invalid, show an error message
            messages.error(request, "Please fill in all required fields correctly.")

    else:
        form = Predict_Form()

    return render(
        request,
        'predict.html',
        {
            'form': form,
            'predicted': predicted,
            'user_id': u_id,
            'predictions': predictions,
            'result': result,
            'colors': colors,
        },
    )