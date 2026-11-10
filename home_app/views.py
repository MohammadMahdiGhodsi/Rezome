

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def home_view(request):
    """صفحه اصلی"""
    context = {
        'profile': {
            'name': 'محمد مهدی قدسی',  # ← اینجا رو به هر چی میخوای تغییر بده
            'title': 'برنامه نویس حرفه‌ای و Network Developer  ',
            'bio': 'من با بیش از 3سال تجربه در زمینه طراحی و برنامه نویسی، مشکلات پیچیده کاربران رو به ساده‌ترین شکل ممکن حل میکنم',
            'email': 'mmdghods07@gmail.com',  # ← ایمیل جدید
            'phone': '+98 938 31 500 31',  # ← شماره جدید
            'address': 'سبزوار، بلوار پاسداران، خیابان دانش آموز ',
        },
        'services': [
            {
                'number': '01',
                'title': 'توسعه وب با جنگو و پایتون',
                'description': 'طراحی و پیاده‌سازی پروژه‌های وب پیشرفته با فریمورک جنگو و زبان پایتون. ایجاد APIهای قدرتمند، سیستم‌های احراز هویت، مدیریت محتوا و اپلیکیشن‌های مقیاس‌پذیر با معماری MVC'
            },
            {
                'number': '02',
                'title': 'مدیریت شبکه و میکروتیک',
                'description': 'پیکربندی و مدیریت تجهیزات میکروتیک، پیاده‌سازی شبکه‌های سازمانی، راه‌اندازی VPN، فایروال، مدیریت پهنای باند، QoS و امنیت شبکه در سطح حرفه‌ای'
            },
            {
                'number': '03',
                'title': 'برنامه‌نویسی Network و اتوماسیون',
                'description': 'توسعه اسکریپت‌های اتوماسیون شبکه با پایتون، مدیریت تجهیزات شبکه با APIهای REST، مانیتورینگ شبکه، تحلیل ترافیک و پیاده‌سازی راهکارهای SDN'
            },
            {
                'number': '04',
                'title': 'مشاوره تخصصی و آموزش',
                'description': 'ارائه مشاوره فنی در حوزه برنامه‌نویسی پایتون، فریمورک جنگو، طراحی شبکه و میکروتیک. آموزش عملی و پروژه‌محور برای تیم‌های توسعه و سازمان‌ها'
            },
        ],
        'experiences': [
            {'title': ' طراحی و توسعه صفر تا صد وبسایت فروشگاهی : Kit-store.ir', 'company': 'خراسان رضوی', 'location': ' سبزوار',
             'start_date': '2026',
             'is_current': False},
            {'title': 'طراحی وب اپلیکیشن حسابرسی  ', 'company': 'خراسان رضوی', 'location': 'مشهد', 'start_date': '2025',
             'is_current': True},

        ],
        'educations': [
            {'degree': ' MTCNA , Network+ , Helpdesk Certificate', 'institution': 'مجتمع فنی حرفه ای تهران',
             'start_date': '2024',
             'end_date': '2025'},
            {'degree': ' Django Certificate  ', 'institution': 'مجتمع فنی حرفه ای تهران', 'start_date': '2024',
             'end_date': '2025'},
            {'degree': 'Python Certificate  ', 'institution': 'مجتمع فنی حرفه ای تهران', 'start_date': '2023',
             'end_date': '2024'},

        ],
        'skills': [
            {'name': 'Python', 'percentage': 92},
            {'name': 'Django', 'percentage': 80},
            {'name': 'MikroTik   ', 'percentage': 85},

        ],

        'funfacts': [
            {'count': '0 ', 'description': 'سابقه <br>کاری'},
            {'count': '5+', 'description': 'پروژه های <br>تکمیل شده'},
            {'count': ' 8.9', 'description': 'میزان <br>رضایت'},
            {'count': '3', 'description': 'سال های <br>تجربیات'},
        ],
    }

    return render(request, 'home_app/index.html', context)


@csrf_exempt
def contact_submit(request):
    """پردازش فرم تماس"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body) if request.content_type == 'application/json' else request.POST

            first_name = data.get('conName', '')
            last_name = data.get('conLName', '')
            email = data.get('conEmail', '')
            phone = data.get('conPhone', '')
            service = data.get('conService', '')
            message = data.get('conMessage', '')

            # چاپ در ترمینال برای دیباگ
            print(f"📩 پیام جدید از: {first_name} {last_name}")
            print(f"📧 ایمیل: {email}")
            print(f"📝 متن: {message}")

            # اینجا میتونی پیام رو توی دیتابیس ذخیره کنی یا ایمیل بفرستی

            return JsonResponse({'success': True, 'message': 'پیام با موفقیت ارسال شد'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)

    return JsonResponse({'success': False, 'message': 'متد مجاز نیست'}, status=405)



