#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : asciidoc
Version  : cd6762bd16b20e5cf19ceaffb8452df912bb5f6e
Release  : 37
URL      : https://github.com/asciidoc/asciidoc-py3/archive/cd6762bd16b20e5cf19ceaffb8452df912bb5f6e.tar.gz
Source0  : https://github.com/asciidoc/asciidoc-py3/archive/cd6762bd16b20e5cf19ceaffb8452df912bb5f6e.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: asciidoc-bin
Requires: asciidoc-data
Requires: asciidoc-license
Requires: asciidoc-man
Requires: docbook-xml
Requires: libxml2-bin
Requires: libxslt
BuildRequires : docbook-xml
BuildRequires : graphviz
BuildRequires : libxml2-dev
BuildRequires : libxslt
BuildRequires : libxslt-dev
BuildRequires : python-core
BuildRequires : python3-dev
BuildRequires : sed
BuildRequires : source-highlight
Patch1: build.patch

%description
Replaced the plain DocBook XSL admonition icons with Jimmac's DocBook
icons (http://jimmac.musichall.cz/ikony.php3). I dropped transparency
from the Jimmac icons to get round MS IE and FOP PNG incompatibilies.

%package bin
Summary: bin components for the asciidoc package.
Group: Binaries
Requires: asciidoc-data
Requires: asciidoc-license
Requires: asciidoc-man

%description bin
bin components for the asciidoc package.


%package data
Summary: data components for the asciidoc package.
Group: Data

%description data
data components for the asciidoc package.


%package license
Summary: license components for the asciidoc package.
Group: Default

%description license
license components for the asciidoc package.


%package man
Summary: man components for the asciidoc package.
Group: Default

%description man
man components for the asciidoc package.


%prep
%setup -q -n asciidoc-py3-cd6762bd16b20e5cf19ceaffb8452df912bb5f6e
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536137479
%reconfigure --disable-static --sysconfdir=/usr/share/asciidoc/conf
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1536137479
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/asciidoc
cp COPYING %{buildroot}/usr/share/doc/asciidoc/COPYING
cp COPYRIGHT %{buildroot}/usr/share/doc/asciidoc/COPYRIGHT
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
/usr/share/asciidoc/conf/asciidoc/filters/graphviz/graphviz-filter.conf
/usr/share/asciidoc/conf/asciidoc/filters/graphviz/graphviz2png.py
/usr/share/asciidoc/conf/asciidoc/filters/latex/latex-filter.conf
/usr/share/asciidoc/conf/asciidoc/filters/latex/latex2img.py
/usr/share/asciidoc/conf/asciidoc/filters/music/music-filter.conf
/usr/share/asciidoc/conf/asciidoc/filters/music/music2png.py
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
/usr/share/asciidoc/conf/asciidoc/lang-fi.conf
/usr/share/asciidoc/conf/asciidoc/lang-fr.conf
/usr/share/asciidoc/conf/asciidoc/lang-hu.conf
/usr/share/asciidoc/conf/asciidoc/lang-id.conf
/usr/share/asciidoc/conf/asciidoc/lang-it.conf
/usr/share/asciidoc/conf/asciidoc/lang-ja.conf
/usr/share/asciidoc/conf/asciidoc/lang-nl.conf
/usr/share/asciidoc/conf/asciidoc/lang-pl.conf
/usr/share/asciidoc/conf/asciidoc/lang-pt-BR.conf
/usr/share/asciidoc/conf/asciidoc/lang-ro.conf
/usr/share/asciidoc/conf/asciidoc/lang-ru.conf
/usr/share/asciidoc/conf/asciidoc/lang-sv.conf
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

%files license
%defattr(-,root,root,-)
/usr/share/doc/asciidoc/COPYING
/usr/share/doc/asciidoc/COPYRIGHT

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/a2x.1
/usr/share/man/man1/asciidoc.1
