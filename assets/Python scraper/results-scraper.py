import requests
from bs4 import BeautifulSoup

# Get the web page
page = requests.get('http://www.sligogaa.ie/FixturesResultsAll.aspx')

# Parse the HTML
soup = BeautifulSoup(page.text, 'html.parser')

# Find the table containing the Bunninadden GAA results
table = soup.find('table', class_="Table")

# Get the rows of the table
rows = table.find_all('tr')

# Create an HTML file called results.html and write the table header
with open('results.html', 'w') as f:
    f.write('<table>\n<tr>\n')
    # Get the headers of the table
    headers = rows[0].find_all('th')
    # Write the table headers to the HTML file
    for header in headers:
        f.write(f'<th>{header.text}</th>\n')
    f.write('</tr>\n')

# Loop through the rows and write their results to the HTML file
for row in rows[1:]:
    with open('results.html', 'a') as f:
        f.write('<tr>\n')
        cells = row.find_all('td')
        # Write the table cells to the HTML file
        for cell in cells:
            f.write(f'<td>{cell.text}</td>\n')
        f.write('</tr>\n')



# open the file in w mode
# set encoding to UTF-8
with open("results.html", "w", encoding = 'utf-8') as file:
    
    # prettify the soup object and convert it into a string  
    file.write(str('<!DOCTYPE html>\n<html lang="en">\n<head>\n\n   <!-- Basic Page Needs\n    ================================================== -->\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n\n    <title>Results | Bunninadden GAA</title>\n\n    <meta name="description" content="">\n    <meta name="author" content="">\n    <meta name="keywords" content="">\n\n    <!-- Mobile Specific Metas\n    ================================================== -->\n    <meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0">\n    <meta name="apple-mobile-web-app-capable" content="yes">\n\n    <!-- Fonts -->\n    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,300i,400,600,700" rel="stylesheet">\n    <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css">\n\n    <!-- Favicon\n    ================================================== -->\n    <link rel="apple-touch-icon" sizes="180x180" href="assets/img/Bunninadden gaa logo.ico">\n    <link rel="icon" type="image/png" sizes="16x16" href="assets/img/Bunninadden gaa logo.ico">\n\n    <!-- Stylesheets\n    ================================================== -->\n    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">\n    <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-black.css">\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/css/font-awesome.min.css">\n    <!-- Bootstrap core CSS -->\n    <link href="assets/css/bootstrap.min.css" rel="stylesheet">\n\n    <!-- Custom styles for this template -->\n    <link href="assets/css/style.css" rel="stylesheet">\n    <link href="assets/css/responsive.css" rel="stylesheet">\n\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\n    <!--[if lt IE 9]>\n    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>\n    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>\n    <![endif]-->\n\n</head>\n<body>\n\n    <header id="masthead" class="site-header site-header-white">\n        <nav id="primary-navigation" class="site-navigation">\n            <div class="container">\n\n                <div class="navbar-header">\n\n                                   </a><img src="/assets/img/bunninadden-icon.webp" alt="Bunninadden GAA Logo"></a>\n\n                </div><!-- /.navbar-header -->\n\n                <div class="collapse navbar-collapse" id="agency-navbar-collapse">\n\n                    <ul class="nav navbar-nav navbar-right">\n\n                        <li><a href="index.html">Home</a></li>\n                        <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Pages<i class="fa fa-caret-down hidden-xs" aria-hidden="true"></i></a>\n\n                            <ul class="dropdown-menu" role="menu" aria-labelledby="menu1">\n                              <li><a href="portfolio.html">Gallery</a></li>\n                              <li><a href="blog.html">Recent News</a></li>\n                              <li><a href="child-protection.html">Child Protection</a></li>\n                              <li><a href="results.html">Results</a></li>\n                            </ul>\n\n                        </li>\n                        <li><a href="portfolio.html">Gallery</a></li>\n                        <li><a href="blog.html">Recent News</a></li>\n                        <li><a href="contact.html">Contact</a></li>\n                        <li><a href="ui-elements.html">History</a></li>\n\n                    </ul>\n\n                </div>\n\n            </div>\n        </nav><!-- /.site-navigation -->\n    </header><!-- /#mastheaed -->\n\n    <div id="hero" class="hero overlay subpage-hero portfolio-hero">\n        <div class="hero-content">\n            <div class="hero-text">\n                <h1>Results</h1>\n                <ol class="breadcrumb">\n                  <li class="breadcrumb-item"><a href="index.html">Home</a></li>\n                  <li class="breadcrumb-item active">Results</li>\n                </ol>\n            </div><!-- /.hero-text -->\n        </div><!-- /.hero-content -->\n    </div><!-- /.hero -->\n\n<!-- ADD API DATA FROM SLIGO GAA SITE BELOW HERE -->\n'))
    file.write('</table>')
    file.write(str('<section>\n    <div align="center"><a class="twitter-timeline" data-width="600" data-dnt="true"  data-tweet-limit="2" data-theme="dark" href="https://twitter.com/bunninaddengaa?ref_src=twsrc%5Etfw">Tweets by bunninaddengaa</a>\n        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>\n        </div>\n</section>\n\n<footer id="colophon" class="site-footer">\n    <div class="container">\n        <div class="row">\n            <div class="col-md-3 col-sm-4 col-xs-6">\n                <a class="site-title"><span>Bunninadden GAA</span></a>\n                <p>We are a small but strong club in the heart of south Sligo.</p>\n                <p>We measure our success by the results we drive for.</p>\n            </div>\n            <div class="col-lg-offset-4 col-md-3 col-sm-4 col-md-offset-2 col-sm-offset-0 col-xs-6 ">\n                <h3>Keep in touch</h3>\n                <ul class="list-unstyled contact-links">\n                    <li><i class="fa fa-envelope" aria-hidden="true"></i><a href="mailto:pro.bunninadden.sligo@gaa.ie">Email PRO</a></li>\n                    <li><i class="fa fa-envelope" aria-hidden="true"></i><a href="mailto:Secretary.bunninadden.sligo@gaa.ie">Email Secretary</a></li>\n                    <li><i class="fa fa-fax" aria-hidden="true"></i><a href="+37400900000">+374 (00) 90 00 00</a></li>\n                    <li><i class="fa fa-map-marker" aria-hidden="true"></i><a href="https://www.google.com/maps/place/Bunninadden+GAA+Club/@54.0389322,-8.5778107,238m/data=!3m1!1e3!4m5!3m4!1s0x0:0xa1095db0f21fe07f!8m2!3d54.0389893!4d-8.5761912">2CQF+JH Bunninadden</a></li>\n                </ul>\n            </div>\n            <div class="clearfix visible-xs"></div>\n            <div class="col-lg-2 col-md-3 col-sm-4 col-xs-6">\n                <h3>Featured links</h3>\n                <ul class="list-unstyled">\n                    <li class="active"><a href="index.html">Home</a></li>\n                    <li><a href="blog.html">Blog</a></li>\n                    <li><a href="portfolio.html">Porfolio</a></li>\n                    <li><a href="contact.html">Contact</a></li>\n                </ul>\n            </div>\n        </div>\n    </div>\n    <div class="copyright">\n        <div class="container">\n            <div class="row">\n                <div class="col-xs-8">\n                    <div class="social-links">\n                        <a class="twitter-bg" href="https://twitter.com/bunninaddengaa?lang=en"><i class="fa fa-twitter"></i>Twitter</a>\n                        <a class="facebook-bg" href="https://www.facebook.com/bunninaddengaaclub/"><i class="fa fa-facebook"></i>Facebook</a>\n                        <!-- <a class="pinterest" href="#"><i class="fa fa-pinterest"></i></a>\n                        <a class="linkedin-bg" href="#"><i class="fa fa-linkedin"></i></a> -->\n                    </div><!-- /.social-links -->\n                </div>\n                <div class="col-xs-4">\n                    <div class="text-right">\n                        <p>&copy; Barry Clavin</p>\n                        <p>All Rights Reserved</p>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div><!-- /.copyright -->\n</footer><!-- /#footer -->\n\n\n<!-- Bootstrap core JavaScript\n================================================== -->\n<!-- Placed at the end of the document so the pages load faster -->\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n<script src="assets/js/bootstrap.min.js"></script>\n<script src="assets/js/bootstrap-select.min.js"></script>\n<script src="assets/js/jquery.slicknav.min.js"></script>\n<script src="assets/js/jquery.countTo.min.js"></script>\n<script src="assets/js/jquery.shuffle.min.js"></script>\n<script src="assets/js/script.js"></script>\n\n</body>\n</html>\n'))

# This code works by first downloading the web page from the given URL and parsing the HTML using the BeautifulSoup library. 
# It then finds the table containing the Bunninadden GAA results and stores the rows of the table in a variable. 
# It then creates an HTML file called results.html and writes the table header to the file. 
# It then loops through the rows and writes each row to the file. Finally, it closes the table in the HTML file.

#python script written with the help of ChatGPT by OpenAI