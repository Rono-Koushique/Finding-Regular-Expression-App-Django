from django.shortcuts import render
import re

def get_matched_spans(pattern, text):
    words = re.finditer(pattern, text)
    spans = []
    for word in words:
        spans.append(list(word.span()))
    return spans

# Create your views here.
def home(request):
    context = {
        'title' : 'Regular Expression Validator'
    }
    if request.method == 'POST':
        text = request.POST['input-text']
        regular_expression = str(request.POST['regular-expression'])
        
        spans = get_matched_spans(regular_expression, text)

        context.update({
            'regular_expression': regular_expression,
            'default_text': text,
            'spans' : spans,
            'match_count' : len(spans),
        })

        return render(request, 'RegExVal/home.html', context)
    else:
        return render(request, 'RegExVal/home.html', context)