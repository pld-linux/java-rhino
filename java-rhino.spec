Summary:	Rhino - JavaScript for Java
Summary(pl):	Rhino - JavaScript dla Javy
Name:		rhino
Version:	1.5R4.1
%define	fver	%(echo %{version} | tr -d .)
%define	dver	%(echo %{version} | tr . _)
Release:	1
License:	NPL 1.1
Group:		Development/Languages/Java
Source0:	ftp://ftp.mozilla.org/pub/js/%{name}%{fver}.zip
# Source0-md5:	f50367530e9860eb4110286bd8ebe175
#BuildRequires:	jakarta-ant
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

%description -l pl
Rhino to implementacja JavaScriptu z otwartymi �r�d�ami napisana
ca�kowicie w Javie. Zwykle jest osadzana w aplikacjach w Javie aby
pozwoli� u�ytkownikom na u�ywanie skrypt�w.

%prep
%setup -q -n %{name}%{dver}

%build
# tries to download something from java.sun.com
#ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install js.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{_javalibdir}/*.jar
