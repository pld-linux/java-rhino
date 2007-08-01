Summary:	Rhino - JavaScript for Java
Summary(pl.UTF-8):	Rhino - JavaScript dla Javy
Name:		rhino
Version:	1.6R6
%define	fver	%(echo %{version} | tr . _)
Release:	1
License:	MPL 1.1 or GPL v2+
Group:		Development/Languages/Java
Source0:	http://ftp.mozilla.org/pub/mozilla.org/js/%{name}%{fver}.zip
# Source0-md5:	03093ee9dbe9d10ce19f274c76c61f8f
URL:		http://www.mozilla.org/rhino/
#BuildRequires:	ant
BuildRequires:	unzip
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

%description -l pl.UTF-8
Rhino to implementacja JavaScriptu z otwartymi źródłami napisana
całkowicie w Javie. Zwykle jest osadzana w aplikacjach w Javie aby
pozwolić użytkownikom na używanie skryptów.

%prep
%setup -q -n %{name}%{fver}

%build
# tries to download jfc from java.sun.com
# tries to download xbean.zip (xmlbeans-2.2.0.zip) from www.apache.org
#ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install js.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc javadoc/*
%{_javalibdir}/*.jar
