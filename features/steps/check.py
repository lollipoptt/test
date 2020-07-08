_author_= 'teenie'
from behave import *
@Given ('I have a letter')
def step_imp(context):
    pass

@When('I input letter {letter}')
def step_imp(context,letter):
    context.letter = letter

@Then('the inputed letter is Equal with {Targetletter')
def step_imp(context,Targetletter):
    context.Targetletter = Targetletter
    assert context.letter is context.Targetletter
