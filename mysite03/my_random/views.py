from django.http import HttpResponse
import random
import string


def random_view(request):
    try:
        length: int = int(request.GET.get("length"), 0)
        # length: int = int(request.values.get('length', 0))
    except Exception:
        length = 0
    try:
        specials: int = int(request.GET.get("specials"), 0)
    except Exception:
        specials = 0
    try:
        digits: int = int(request.GET.get("digits"), 0)
    except Exception:
        digits = 0
    alphabet: str = string.ascii_lowercase + string.ascii_uppercase
    spec = '!"№;%:?*()_+'
    digits_list = '0123456789'
    if specials == 1:
        alphabet += spec
    if digits == 1:
        alphabet += digits_list
    res = []
    if length is not None and range(1, 100):
        for i in range(length):
            res.append(random.choice(alphabet))

    result_string = ''.join(res)
    return HttpResponse(f"""
<!DOCTYPE html>
        <html>
        <head>      
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity=
        "sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <title>Random string</title>    
        </head>    
            
        <body>
        <div class="container-lg">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="http://127.0.0.1:8000/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://127.0.0.1:8000/about/whoami/">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/about/source_code">Source code</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://127.0.0.1:8000/random/?length=42&specials=1&digits=0">Generate random string</a>
        </li>
        </ul>   
        </div>
        <div class="container-lg">
        <p >
        <h3>Generate string</h3><br/>
        <div class="mb-3">
    <label for="exampleFormControlTextarea1" class="form-label">Your string:</label>
    <textarea class="form-control" id="exampleFormControlTextarea1" rows="10">{result_string}</textarea>
    </div>
        </p>
        </div>
        </body>
        </html>
    """)