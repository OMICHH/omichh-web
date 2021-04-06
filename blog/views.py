from django.shortcuts import render

# Create your views here.

def blog_view(request):

    # Dummy data
    posts = [
        {
            'title' : 'Soy el primer titulo',
            'description' : 'Soy la descripción del primero',
            'date' : '18/02/2021',
            'url' : '#'
        },
        {
            'title' : 'Soy el segundo titulo',
            'description' : 'Soy la descripción del segundo',
            'date' : '26/02/2021',
            'url' : '#'
        },
        {
            'title' : '"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."',
            'description' : 'ta bn',
            'date' : '02/03/2021',
            'url' : '#'
        },
        {
            'title' : 'mini titulo',
            'description' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sollicitudin ultricies dolor, scelerisque facilisis ante finibus nec.',
            'date' : '??/??/????',
            'url' : '#'
        },
        {
            'title' : 'Soy un filler',
            'description' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'date' : '??/??/????',
            'url' : '#'
        },
        {
            'title' : 'Soy un filler',
            'description' : 'Soy la descripción del filler',
            'date' : '??/??/????',
            'url' : '#'
        },
        {
            'title' : 'Soy un filler',
            'description' : 'Soy la descripción del filler',
            'date' : '??/??/????',
            'url' : '#'
        }
    ]

    context = {
        'posts' : posts
    }

    return render(request, 'blog/blog.html', context)
