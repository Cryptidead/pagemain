from django.shortcuts import render

html_base = """
<h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/contact/">Contacto</a></li>
    </ul>
"""

def home(request):
    return HttpResponse(html_base + """
        <h2>Bienvenidos</h2>
        <p>Esto es la portada.</p>
    """)

def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Me llamo Héctor y me encanta Django!</p>
    """)

def contact(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Aquí os dejo mi email y mis redes sociales:</p>
        <ul>
            <li><a href="mailto:hola@hektorprofe.net">Email</a></li>
            <li><a href="https://github.com/hcosta">Github</a></li>
            <li><a href="https://youtube.com">Youtube</a></li>
        </ul>
    """)



















 <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>{% block title %}{% endblock %} | Pruebas</title>
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <!-- Font Awesome icons (free version)-->
        <script src="https://use.fontawesome.com/releases/v5.15.4/js/all.js" crossorigin="anonymous"></script>
        <!-- Google fonts-->
        <link href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic" rel="stylesheet" type="text/css" />
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800" rel="stylesheet" type="text/css" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body>
                <!-- Navigation-->
         <nav class="navbar navbar-expand-lg navbar-light" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="{% url 'home' %}">Pruebas</a>
                
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    Menu
                    <i class="fas fa-bars"></i>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ml-auto py-4 py-lg-0">
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="{% url 'home' %}">Portada</a></li>
                        <li class="nav-item"><a class="nav-link  px-lg-3 py-3 py-lg-4" href="{% url 'about' %}">Acerca de</a></li>
                        <li class="nav-item"><a class="nav-link  px-lg-3 py-3 py-lg-4" href="{% url 'portafolio'%}">Portafolio</a></li>
                        <li class="nav-item"><a class="nav-link  px-lg-3 py-3 py-lg-4" href="{% url 'contact'%}">Contacto</a>
                        <li class="nav-item"><a class="nav-link  px-lg-3 py-3 py-lg-4" href="{% url 'login'%}">Inicio de sesión</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>   

        <!-- Cabecera -->
       
        <!-- Page Header-->
        <header class="masthead" style="background-image: url('{%block background%}{%endblock%}')">
            <div class="overlay"></div>
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 col-md-10 mx-auto">
                        <div class="site-heading">{% block headers %}{% endblock %}</div>
                    </div>

                    <!-- Navigation-->
         <nav class="navbar navbar-expand-lg navbar-light" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="{% url 'home' %}">Pruebas</a>
                
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    Menu
                    <i class="fas fa-bars"></i>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ml-auto py-4 py-lg-0">
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="{% url 'home' %}">Portada</a></li>
                        <li class="nav-item"><a class="nav-link  px-lg-3 py-3 py-lg-4" href="{% url 'about' %}">Acerca de</a></li>
                        <li class="nav-item"><a class="nav-link  px-lg-3 py-3 py-lg-4" href="{% url 'portafolio'%}">Portafolio</a></li>
                        <li class="nav-item"><a class="nav-link  px-lg-3 py-3 py-lg-4" href="{% url 'contact'%}">Contacto</a>
                        <li class="nav-item"><a class="nav-link  px-lg-3 py-3 py-lg-4" href="{% url 'login'%}">Inicio de sesión</a>
                        <li class="nav-item"><a class="nav-link  px-lg-3 py-3 py-lg-4" href="{% url 'logout'%}">Cerrar sesión</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>  
                    
                </div>
            </div>
        </header>

           <!-- Main Content-->
           <div class="container px-4 px-lg-5">
            <div class="row gx-4 gx-lg-5 justify-content-left">
                <div class="col-md-10 col-lg-8 col-xl-7">
                    {% block content %}{% endblock %}
                </div>
            </div>
        </div>

        {% if request.path != "/" %}<hr></hr>{% endif %}

        
                 
            


        <!-- Estilos y fuentes del template -->
        {% load static %}
        <link href="{% static 'core/vendor/bootstrap/css/bootstrap.min.css'%}" rel="stylesheet">
        <link href="{% static 'core/vendor/font-awesome/css/fontawesome.min.css' %}" rel="stylesheet" type="text/css">
        <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
        <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800'rel='stylesheet' type='text/css'>
        <link href="{% static 'core/css/clean-blog.min.css' %}"rel="stylesheet">

        <!-- Bootstrap y Javascripts -->
        <script src="{% static 'core/vendor/jquery/jquery.min.js'%}"></script>
        <script src="{% static
            'core/vendor/bootstrap/js/bootstrap.bundle.min.js' %}"></script>
        <script src="{% static 'core/js/clean-blog.min.js' %}"></script>

        <!-- Footer-->
        <footer class="border-top">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-7">
                        <ul class="list-inline text-center">
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                        </ul>
                        <div class="small text-center text-muted fst-italic">Copyright &copy; Your Website 2021</div>
                    </div>
                </div>
            </div>
        </footer>
        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
    </body>
</html>

   