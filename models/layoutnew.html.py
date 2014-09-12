<!--[if HTML5]><![endif]-->
<!DOCTYPE html>
<!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->
<!--[if lt IE 7]><html class="ie ie6 ie-lte9 ie-lte8 ie-lte7 no-js" lang="{{=T.accepted_language or 'en'}}"> <![endif]-->
<!--[if IE 7]><html class="ie ie7 ie-lte9 ie-lte8 ie-lte7 no-js" lang="{{=T.accepted_language or 'en'}}"> <![endif]-->
<!--[if IE 8]><html class="ie ie8 ie-lte9 ie-lte8 no-js" lang="{{=T.accepted_language or 'en'}}"> <![endif]-->
<!--[if IE 9]><html class="ie9 ie-lte9 no-js" lang="{{=T.accepted_language or 'en'}}"> <![endif]-->
<!--[if (gt IE 9)|!(IE)]><!--> <html class="no-js" lang="{{=T.accepted_language or 'en'}}"> <!--<![endif]-->
<head>

  <!--[if !HTML5]>
      <meta http-equiv="X-UA-Compatible" content="IE=edge{{=not request.is_local and ',chrome=1' or ''}}">
  <![endif]-->
  <!-- www.phpied.com/conditional-comments-block-downloads/ -->
  <!-- Always force latest IE rendering engine
       (even in intranet) & Chrome Frame
       Remove this if you use the .htaccess -->
	   
  <meta charset="utf-8" />

  <!-- http://dev.w3.org/html5/markup/meta.name.html -->
  <meta name="application-name" content="{{=request.application}}" />

  <!-- Speaking of Google, don't forget to set your site up:
       http://google.com/webmasters -->
  <meta name="google-site-verification" content="" />

  <!--  Mobile Viewport Fix
        j.mp/mobileviewport & davidbcalhoun.com/2010/viewport-metatag
        device-width: Occupy full width of the screen in its current orientation
        initial-scale = 1.0 retains dimensions instead of zooming out if page height > device height
        user-scalable = yes allows the user to zoom in -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <link rel="shortcut icon" href="{{=URL('static','images/favicon.ico')}}" type="image/x-icon">
  <link rel="apple-touch-icon" href="{{=URL('static','images/favicon.png')}}">

  <!-- All JavaScript at the bottom, except for Modernizr which enables
       HTML5 elements & feature detects -->
  <script src="{{=URL('static','js/modernizr.custom.js')}}"></script>

  <!-- include stylesheets -->
  {{
  response.files.insert(0,URL('static','css/web2py.css'))
  response.files.insert(1,URL('static','css/bootstrap.min.css'))
  response.files.insert(2,URL('static','css/bootstrap-responsive.min.css'))
  response.files.insert(3,URL('static','css/web2py_bootstrap.css'))
  }}

  {{include 'web2py_ajax.html'}}

  {{
  # using sidebars need to know what sidebar you want to use
  left_sidebar_enabled = globals().get('left_sidebar_enabled',False)
  right_sidebar_enabled = globals().get('right_sidebar_enabled',False)
  middle_columns = {0:'span12',1:'span9',2:'span6'}[
    (left_sidebar_enabled and 1 or 0)+(right_sidebar_enabled and 1 or 0)]
  }}

  <!-- uncomment here to load jquery-ui
       <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/themes/ui-lightness/jquery-ui.css" type="text/css" media="all" />
       <script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js" type="text/javascript"></script>
       uncomment to load jquery-ui //-->
  <noscript><link href="{{=URL('static', 'css/web2py_bootstrap_nojs.css')}}" rel="stylesheet" type="text/css" /></noscript>
  {{block head}}{{end}}
</head>

<body>


  <div class="container">
  
    <section id="main" class="main row">
        {{if left_sidebar_enabled:}}
        <div class="span3 left-sidebar">
            {{block left_sidebar}}
            <h3>Left Sidebar</h3>
            <p></p>
            {{end}}
        </div>
        {{pass}}

        <div class="{{=middle_columns}}">
            {{block center}}
            {{include}}
            {{end}}
        </div>

        {{if right_sidebar_enabled:}}
        <div class="span3">
            {{block right_sidebar}}
            <h3>Right Sidebar</h3>
            <p></p>
            {{end}}
        </div>
        {{pass}}
    </section><!--/main-->

  

  </div> <!-- /container -->

  <!-- The javascript =============================================
       (Placed at the end of the document so the pages load faster) -->
  <script src="{{=URL('static','js/bootstrap.min.js')}}"></script>
  <script src="{{=URL('static','js/web2py_bootstrap.js')}}"></script>
  <!--[if lt IE 7 ]>
      <script src="{{=URL('static','js/dd_belatedpng.js')}}"></script>
      <script> DD_belatedPNG.fix('img, .png_bg'); //fix any <img> or .png_bg background-images </script>
      <![endif]-->
  
  {{if response.google_analytics_id:}}
  <script src="{{=URL('static','js/analytics.min.js')}}"></script>
  <script type="text/javascript">
  analytics.initialize({
    'Google Analytics':{trackingId:'{{=response.google_analytics_id}}'} 
  });</script>
  {{pass}}
  <script src="{{=URL('static','js/share.js',vars=dict(static=URL('static','images')))}}"></script>
</body>
</html>
