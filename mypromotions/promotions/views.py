from django.shortcuts import render

promotionItems = [
    {
        'id': 1,
        'title': 'Promotion 1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam hendrerit, metus vel condimentum pharetra, mi leo posuere risus, placerat faucibus nisl purus sed metus. Sed pellentesque mollis diam. ',
        'image': 'https://picsum.photos/200',
        'price': 100
    },
    {
        'id': 2,
        'title': 'Promotion 2',
        'description': 'Curabitur feugiat vel ipsum ut egestas. Aenean feugiat sapien ex, eget dictum nunc gravida vitae. Nunc dapibus tincidunt mi auctor tempor.',
        'image': 'https://picsum.photos/200',
        'price': 200
    },
    {
        'id': 3,
        'title': 'Promotion 3',
        'description': 'Duis interdum nulla mi, vitae vehicula nisl luctus sit amet. Vestibulum euismod, magna non luctus aliquet, tellus justo tincidunt nisl, vitae dignissim sapien eros in nisl.',
        'image': 'https://picsum.photos/200',
        'price': 300
    },
    {
        'id': 4,
        'title': 'Promotion 4',
        'description': 'Nulla facilisi. Donec vitae dui euismod, pretium nulla id, tempor nibh. Donec dapibus sapien nec erat efficitur, at dignissim justo luctus.',
        'image': 'https://picsum.photos/200',
        'price': 270.89
    },
    {
        'id': 5,
        'title': 'Promotion 5', 
        'description': 'Nulla facilisi. Donec vitae dui euismod, pretium nulla id, tempor nibh. Donec dapibus sapien nec erat efficitur, at dignissim justo luctus.',
        'image': 'https://picsum.photos/200',
        'price': 170.89
    }
]

# Create your views here.
def index(request):
    return render(request, 'promotions.html', {'promotionItems': promotionItems})

def details(request, promotion_id):
    return render(request, 'details.html', {'promotion_id': promotionItems[promotion_id-1]})