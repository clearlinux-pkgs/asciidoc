#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : asciidoc
Version  : 8.6.9
Release  : 22
URL      : https://sourceforge.net/projects/asciidoc/files/asciidoc/8.6.9/asciidoc-8.6.9.tar.gz
Source0  : https://sourceforge.net/projects/asciidoc/files/asciidoc/8.6.9/asciidoc-8.6.9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: asciidoc-bin
Requires: asciidoc-data
Requires: asciidoc-doc
BuildRequires : graphviz
BuildRequires : python-dev
BuildRequires : sed
BuildRequires : source-highlight

%description
version 8.6.9, 9 November 2013
__________________________________________________________________

%package bin
Summary: bin components for the asciidoc package.
Group: Binaries
Requires: asciidoc-data

%description bin
bin components for the asciidoc package.


%package data
Summary: data components for the asciidoc package.
Group: Data

%description data
data components for the asciidoc package.


%package doc
Summary: doc components for the asciidoc package.
Group: Documentation

%description doc
doc components for the asciidoc package.


%prep
%setup -q -n asciidoc-8.6.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1509381869
%configure --disable-static --sysconfdir=/usr/share/asciidoc/conf
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python ./tests/testasciidoc.py update ; python ./tests/testasciidoc.py run

%install
export SOURCE_DATE_EPOCH=1509381869
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/a2x
/usr/bin/a2x.py
/usr/bin/asciidoc
/usr/bin/asciidoc.py

%files data
%defattr(-,root,root,-)
/usr/share/asciidoc/conf/asciidoc/asciidoc.conf
/usr/share/asciidoc/conf/asciidoc/dblatex/asciidoc-dblatex.sty
/usr/share/asciidoc/conf/asciidoc/dblatex/asciidoc-dblatex.xsl
/usr/share/asciidoc/conf/asciidoc/docbook-xsl/chunked.xsl
/usr/share/asciidoc/conf/asciidoc/docbook-xsl/common.xsl
/usr/share/asciidoc/conf/asciidoc/docbook-xsl/epub.xsl
/usr/share/asciidoc/conf/asciidoc/docbook-xsl/fo.xsl
/usr/share/asciidoc/conf/asciidoc/docbook-xsl/htmlhelp.xsl
/usr/share/asciidoc/conf/asciidoc/docbook-xsl/manpage.xsl
/usr/share/asciidoc/conf/asciidoc/docbook-xsl/text.xsl
/usr/share/asciidoc/conf/asciidoc/docbook-xsl/xhtml.xsl
/usr/share/asciidoc/conf/asciidoc/docbook45.conf
/usr/share/asciidoc/conf/asciidoc/filters/code/code-filter.conf
/usr/share/asciidoc/conf/asciidoc/filters/code/code-filter.py
/usr/share/asciidoc/conf/asciidoc/filters/code/code-filter.pyc
/usr/share/asciidoc/conf/asciidoc/filters/graphviz/graphviz-filter.conf
/usr/share/asciidoc/conf/asciidoc/filters/graphviz/graphviz2png.py
/usr/share/asciidoc/conf/asciidoc/filters/graphviz/graphviz2png.pyc
/usr/share/asciidoc/conf/asciidoc/filters/latex/latex-filter.conf
/usr/share/asciidoc/conf/asciidoc/filters/latex/latex2png.py
/usr/share/asciidoc/conf/asciidoc/filters/latex/latex2png.pyc
/usr/share/asciidoc/conf/asciidoc/filters/music/music-filter.conf
/usr/share/asciidoc/conf/asciidoc/filters/music/music2png.py
/usr/share/asciidoc/conf/asciidoc/filters/music/music2png.pyc
/usr/share/asciidoc/conf/asciidoc/filters/source/source-highlight-filter.conf
/usr/share/asciidoc/conf/asciidoc/help.conf
/usr/share/asciidoc/conf/asciidoc/html4.conf
/usr/share/asciidoc/conf/asciidoc/html5.conf
/usr/share/asciidoc/conf/asciidoc/images/icons/README
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/1.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/10.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/11.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/12.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/13.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/14.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/15.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/2.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/3.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/4.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/5.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/6.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/7.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/8.png
/usr/share/asciidoc/conf/asciidoc/images/icons/callouts/9.png
/usr/share/asciidoc/conf/asciidoc/images/icons/caution.png
/usr/share/asciidoc/conf/asciidoc/images/icons/example.png
/usr/share/asciidoc/conf/asciidoc/images/icons/home.png
/usr/share/asciidoc/conf/asciidoc/images/icons/important.png
/usr/share/asciidoc/conf/asciidoc/images/icons/next.png
/usr/share/asciidoc/conf/asciidoc/images/icons/note.png
/usr/share/asciidoc/conf/asciidoc/images/icons/prev.png
/usr/share/asciidoc/conf/asciidoc/images/icons/tip.png
/usr/share/asciidoc/conf/asciidoc/images/icons/up.png
/usr/share/asciidoc/conf/asciidoc/images/icons/warning.png
/usr/share/asciidoc/conf/asciidoc/javascripts/ASCIIMathML.js
/usr/share/asciidoc/conf/asciidoc/javascripts/LaTeXMathML.js
/usr/share/asciidoc/conf/asciidoc/javascripts/asciidoc.js
/usr/share/asciidoc/conf/asciidoc/javascripts/slidy.js
/usr/share/asciidoc/conf/asciidoc/javascripts/toc.js
/usr/share/asciidoc/conf/asciidoc/lang-cs.conf
/usr/share/asciidoc/conf/asciidoc/lang-de.conf
/usr/share/asciidoc/conf/asciidoc/lang-el.conf
/usr/share/asciidoc/conf/asciidoc/lang-en.conf
/usr/share/asciidoc/conf/asciidoc/lang-es.conf
/usr/share/asciidoc/conf/asciidoc/lang-fr.conf
/usr/share/asciidoc/conf/asciidoc/lang-hu.conf
/usr/share/asciidoc/conf/asciidoc/lang-it.conf
/usr/share/asciidoc/conf/asciidoc/lang-nl.conf
/usr/share/asciidoc/conf/asciidoc/lang-pt-BR.conf
/usr/share/asciidoc/conf/asciidoc/lang-ro.conf
/usr/share/asciidoc/conf/asciidoc/lang-ru.conf
/usr/share/asciidoc/conf/asciidoc/lang-uk.conf
/usr/share/asciidoc/conf/asciidoc/latex.conf
/usr/share/asciidoc/conf/asciidoc/slidy.conf
/usr/share/asciidoc/conf/asciidoc/stylesheets/asciidoc.css
/usr/share/asciidoc/conf/asciidoc/stylesheets/docbook-xsl.css
/usr/share/asciidoc/conf/asciidoc/stylesheets/pygments.css
/usr/share/asciidoc/conf/asciidoc/stylesheets/slidy.css
/usr/share/asciidoc/conf/asciidoc/stylesheets/toc2.css
/usr/share/asciidoc/conf/asciidoc/stylesheets/xhtml11-quirks.css
/usr/share/asciidoc/conf/asciidoc/text.conf
/usr/share/asciidoc/conf/asciidoc/themes/flask/flask.css
/usr/share/asciidoc/conf/asciidoc/themes/volnitsky/volnitsky.css
/usr/share/asciidoc/conf/asciidoc/xhtml11-quirks.conf
/usr/share/asciidoc/conf/asciidoc/xhtml11.conf

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
