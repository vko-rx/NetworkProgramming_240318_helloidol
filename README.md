# helloidol

---

1. startproject helloidol
   1. python -m pip install django~=4.2
   2. django-admin startproject _helloidol_ .
   3. [python manage.py migrate]
   4. python manage.py runserver
2. startapp _playground_
   1. Terminal
      1. python manage.py startapp _playground_
   2. helloidol/settings.py
      1. 'playground', in INSTALLED_APPS
3. playground/
   - 정보 전달: urls -> views -> (models -> )templates
   - 코드 작성: (models -> )views -> templates -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
      3. _say_bye_html()_
      4. -> templates에 context 전달
   2. urls
      1. _playground/hello/_ -> _say_hello()_
      2. _playground/hello_html/_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloidol/
   1. urls, playground/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
      3. _playground/_ -> _bye_html/_ -> _say_bye_html()_
---
5. startapp 무드
   1. Terminal
      1. python manage.py startapp MOOD
   2. helloidol/settings.py
      1. 'MOOD', in INSTALLED_APPS
6. MOOD/
   1. views
      1. show_ksw()
      2. show_ajw()
      3. -> templates에 context 전달
      4. 정보를 하나로 묶고, 거기에서 꺼내오자
   2. templates/MOOD/
      1. ~~ksw.html~~
         1. title: MOOD - ksw
         2. h1: MOOD
         3. h2: 강신우
         4. img: 강신우 프로필 사진
            1. border_radius: 50%;
      2. ~~ajy.html~~
      3. member.html
         1. group_name, name, img_src
   3. urls
      1. MOOD/ -> ksw -> show_ksw()
      2. MOOD/ -> ajy -> show_ajy()





