from django.shortcuts import render
import qrcode
from qrcode.image import svg
from io import BytesIO
from django.utils.timezone import now

# Create your views here.


def home(request):
    context = {}
    if request.method == "POST":
        qr_code_factory = svg.SvgImage
        image = qrcode.make(request.POST.get('qr-text', ''), version=3,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            image_factory=qr_code_factory, box_size=30, border=2)
        stream = BytesIO()

        image.save(stream)
        context['svg'] = stream.getvalue().decode()
        return render(request, 'home.html', context)
    return render(request, 'home.html', context)

