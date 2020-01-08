# django_recipes
Various Django patterns mostly based on class based views

Each 'recipe' is contained in a single application under the project django_recipes

**CONTENTS**

**_1) Campaign_**

The example use-case has the following scenario:

You have a landing page which corresponds to a campain you are running, you want to have a signup form on this page to capture
email addresses of interested users, store them in a database and possibly follow up with confirmation email etc. When the users sign up
you need to know which campaign page they have signed up from.

This scenario requires that DetailView (representing the campaign object) is combined with a form.
The chosen method is to use DetailView to display the campaign, and FormView/SingleObjectMixin to handle the form.
In views.py three classes are created
  CampaignDisplayView(DetailView) - handling the campaign detail
  CampaignSignupView(FormView, SingleObjectMixin) - handling the signup form
  CampaignDetailView(View) - combining the above to into a single multipurpose view
  
The underlying models are Campaign and Subscriber, the signup form is underlain by a ModelForm called
SubscriberSignupForm.
  
The trick is to override form_valid in the CampaignSignupView in order to pass the campaign pk to the
SubscriberSignupForm's save method.

In real-life the signup form should only activate after the user has consented and read a privacy policy. In addition any emails and names 
should be stored in encrypted form.
