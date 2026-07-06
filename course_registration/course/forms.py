# from django import forms
# from .models import Course

# class Courseform(forms.ModelForm):
#     class Meta:
#         model=Course
#         fields=['course_code','course_name','description','instructor','duration','credit']
#     def clean_course_name(self):
#         course_name=self.cleaned_data['course_name']
#         if len(course_name)<3:
#             raise forms.ValidationError("Course Name Must Greater than 3 letter")
#     def clean_course_duration(self):
#         course_duration=self.cleaned_data['course_duration']
#         if duration==0:
#             raise forms.ValidationError("Course Duration Must Greater than 0")
#     def clean_course_credit(self):


#         course_credit=self.cleaned_data['course_credit']
#         if credit<1 and credit>10:
#             raise forms.ValidationError("Course Credit Must be between 1 to 10")

from django import forms
from .models import Course

class Courseform(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name', 'description', 'instructor', 'duration', 'credit']

    # 1. Clean Course Name
    def clean_course_name(self):
        course_name = self.cleaned_data.get('course_name')
        if course_name and len(course_name) < 3:
            raise forms.ValidationError("Course Name Must Greater than 3 letters")
        return course_name  # Required: Always return the cleaned data

    # 2. Clean Duration (Method name must match the field 'duration')
    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if duration is not None and duration <= 0:
            raise forms.ValidationError("Course Duration Must Greater than 0")
        return duration  # Required: Always return the cleaned data

    # 3. Clean Credit (Method name must match the field 'credit')
    def clean_credit(self):
        credit = self.cleaned_data.get('credit')
        # Logic fix: Use 'or' instead of 'and' because a number cannot be less than 1 AND greater than 10 at the same time
        if credit is not None and (credit < 1 or credit > 10):
            raise forms.ValidationError("Course Credit Must be between 1 to 10")
        return credit  # Required: Always return the cleaned data
    def clean(self):
        cleaned_data=super().clean()
        duration=self.cleaned_data['duration']
        credit=self.cleaned_data['credit']

        if duration and credit:
            if duration< credit:
                raise forms.ValidationError("Duration Must Have Greater than Credit")
        return cleaned_data
        