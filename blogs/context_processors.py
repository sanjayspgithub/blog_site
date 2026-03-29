from .models import Category, Social


# to show the category all over website every single page
def categories_processor(request):
    return {
        'categories': Category.objects.all()
    }



# to show the link all over website every single page
# def social_link(request):
#     return{
#         'social_link': Social.objects.all()
#     }