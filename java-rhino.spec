# TODO
# - skip building old XMLBeans-based implementation of E4X? (see prep section)
%define		fver	%(echo %{version} | tr . _)
%include	/usr/lib/rpm/macros.java
Summary:	Rhino - JavaScript for Java
Summary(pl.UTF-8):	Rhino - JavaScript dla Javy
Name:		java-rhino
Version:	1.7R3
Release:	1
License:	MPL 1.1 or GPL v2+
Group:		Development/Languages/Java
Source0:	http://ftp.mozilla.org/pub/mozilla.org/js/rhino%{fver}.zip
# Source0-md5:	99d94103662a8d0b571e247a77432ac5
Source1:	http://java.sun.com/products/jfc/tsc/articles/treetable2/downloads/src.zip
# Source1-md5:	ab016c8f81812bb930fc0f7a69e053c5
Source2:	http://www.apache.org/dist/xmlbeans/binaries/xmlbeans-2.2.0.zip
# Source2-md5:	f279d25e2dccbb524e406543c38b4aae
URL:		http://www.mozilla.org/rhino/
BuildRequires:	ant
BuildRequires:	jdk >= 1.5
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jpackage-utils
Obsoletes:	rhino
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

%description -l pl.UTF-8
Rhino to implementacja JavaScriptu z otwartymi źródłami napisana
całkowicie w Javie. Zwykle jest osadzana w aplikacjach w Javie aby
pozwolić użytkownikom na używanie skryptów.

%package javadoc
Summary:	Online manual for Rhino
Summary(pl.UTF-8):	Dokumentacja online do Rhino
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for Rhino.

%description javadoc -l pl.UTF-8
Dokumentacja do Rhino.

%description javadoc -l fr.UTF-8
Javadoc pour Rhino.

%prep
%setup -q -n rhino%{fver}

cat <<'EOF' >> build.properties
# use local path
swing-ex-url=file:%{SOURCE1}
# use local path
xmlbeans.zip=%{SOURCE2}

# Will cause E4X not to be built
#no-e4x=true
# Will cause the old, XMLBeans-based implementation of E4X not to be built
#no-xmlbeans=true
EOF

%build
# workaround for java-gcj-compat-devel compilation failure
%ant jar || :
%{__rm} build/classes/org/mozilla/javascript/{FieldAndMethods,JavaMembers}.class

%ant jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
install build/rhino%{fver}/js.jar $RPM_BUILD_ROOT%{_javadir}/js-%{version}.jar
ln -s js-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/js.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/js-%{version}.jar
%{_javadir}/js.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
