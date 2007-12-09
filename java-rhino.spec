%include	/usr/lib/rpm/macros.java
%define	fver	%(echo %{version} | tr . _)
Summary:	Rhino - JavaScript for Java
Summary(pl.UTF-8):	Rhino - JavaScript dla Javy
Name:		rhino
Version:	1.6R7
Release:	1
License:	MPL 1.1 or GPL v2+
Group:		Development/Languages/Java
Source0:	http://ftp.mozilla.org/pub/mozilla.org/js/%{name}%{fver}.zip
# Source0-md5:	7be259ae496aae78feaafe7099e09897
URL:		http://www.mozilla.org/rhino/
#BuildRequires:	ant
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jpackage-utils
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
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{name} -

%description javadoc -l fr.UTF-8
Javadoc pour %{name}.

%prep
%setup -q -n %{name}%{fver}

%build
# tries to download jfc from java.sun.com
# tries to download xbean.zip (xmlbeans-2.2.0.zip) from www.apache.org
#ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
install js.jar $RPM_BUILD_ROOT%{_javadir}/js-%{version}.jar
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
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
