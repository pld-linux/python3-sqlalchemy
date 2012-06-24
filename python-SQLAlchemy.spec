Summary:	Database Abstraction Library
Summary(pl):	Biblioteka abstrakcji baz danych
Name:		python-SQLAlchemy
Version:	0.3.1
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/S/SQLAlchemy/SQLAlchemy-%{version}.tar.gz
# Source0-md5:	cb5e17096ed50389687c62bad8c5a67a
URL:		http://www.sqlalchemy.org/
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6-0.a9.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL.
SQLAlchemy provides a full suite of well known enterprise-level
persistence patterns, designed for efficient and high-performing
database access, adapted into a simple and Pythonic domain language.

%description -l pl
Zestaw narz�dzi SQL dla Pythona oraz odwzorowa� obiektowo-relacyjnych
daj�cych programistom ca�� pot�g� i elastyczno�� SQL-a. SQLAlchemy
udost�pnia pe�ny zbi�r dobrze znanych wzorc�w trwa�o�ci,
zaprojektowanych do wydajnego dost�pu do baz danych, zaadoptowanych do
prostej, pythonowej domeny j�zykowej.

%prep
%setup -q -n SQLAlchemy-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES doc/*html examples/
%{py_sitescriptdir}/SQLAlchemy*
%{py_sitescriptdir}/sqlalchemy*
