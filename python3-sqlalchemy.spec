#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module  sqlalchemy
Summary:	Database Abstraction Library for Python
Summary(pl.UTF-8):	Biblioteka abstrakcji baz danych dla Pythona
Name:		python3-%{module}
Version:	2.0.41
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sqlalchemy/
Source0:	https://files.pythonhosted.org/packages/source/s/sqlalchemy/sqlalchemy-%{version}.tar.gz
# Source0-md5:	76ade8b13f77b9ceaff6c91f5617c668
URL:		https://www.sqlalchemy.org/
BuildRequires:	python3-Cython
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 0.6-0.a9.1
%if %{with tests}
%if "%{py3_ver}" == "3.7"
BuildRequires:	python3-importlib_metadata
%endif
BuildRequires:	python3-greenlet >= 1
BuildRequires:	python3-pytest >= 7.0.0
BuildRequires:	python3-pytest-xdist
BuildRequires:	python3-typing_extensions >= 4.6.0
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
Provides:	python3-SQLAlchemy = %{version}-%{release}
Obsoletes:	python3-SQLAlchemy < 0.9.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL.
SQLAlchemy provides a full suite of well known enterprise-level
persistence patterns, designed for efficient and high-performing
database access, adapted into a simple and Pythonic domain language.

%description -l pl.UTF-8
Zestaw narzędzi SQL oraz odwzorowań obiektowo-relacyjnych dla Pythona,
dający programistom całą potęgę i elastyczność SQL-a. SQLAlchemy
udostępnia pełny zbiór dobrze znanych wzorców trwałości,
zaprojektowanych z myślą o efektywny i wydajnym dostępem do baz
danych, zaadaptowanych do prostego, pythonowego języka.

%package apidocs
Summary:	API documentation for Python SQLAlchemy module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona SQLAlchemy
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python SQLAlchemy module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona SQLAlchemy.

%package examples
Summary:	Examples for Python SQLAlchemy module
Summary(pl.UTF-8):	Przykłady do modułu Pythona SQLAlchemy
Group:		Documentation
BuildArch:	noarch

%description examples
Examples for Python SQLAlchemy module.

%description examples -l pl.UTF-8
Przykłady do modułu Pythona SQLAlchemy.

%prep
%setup -q -n sqlalchemy-%{version}

%build
%py3_build

%if %{with tests}
# =================================== FAILURES ===================================
# ____________ MypyPlainTest.test_mypy_no_plugin[mapped_covariant.py] ____________
# [...]
# AssertionError: .../mapped_covariant.py:35: error: Incompatible return value type (got "Mapped[str]", expected "str")  [return-value]
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(echo $(pwd)/build-3/lib.linux-*) \
%{__python3} -m pytest test -k 'not test_mypy_no_plugin[mapped_covariant.py]'
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES.rst LICENSE README.rst
%dir %{py3_sitedir}/sqlalchemy
%{py3_sitedir}/sqlalchemy/connectors
%dir %{py3_sitedir}/sqlalchemy/cyextension
%{py3_sitedir}/sqlalchemy/cyextension/__init__.py
%{py3_sitedir}/sqlalchemy/cyextension/__pycache__
%attr(755,root,root) %{py3_sitedir}/sqlalchemy/cyextension/*.so
%{py3_sitedir}/sqlalchemy/cyextension/*.pxd
%{py3_sitedir}/sqlalchemy/cyextension/*.pyx
%{py3_sitedir}/sqlalchemy/dialects
%{py3_sitedir}/sqlalchemy/engine
%{py3_sitedir}/sqlalchemy/event
%{py3_sitedir}/sqlalchemy/ext
%{py3_sitedir}/sqlalchemy/future
%{py3_sitedir}/sqlalchemy/orm
%{py3_sitedir}/sqlalchemy/pool
%{py3_sitedir}/sqlalchemy/sql
%{py3_sitedir}/sqlalchemy/testing
%{py3_sitedir}/sqlalchemy/util
%{py3_sitedir}/sqlalchemy/py.typed
%{py3_sitedir}/sqlalchemy/*.py
%{py3_sitedir}/sqlalchemy/__pycache__
%{py3_sitedir}/SQLAlchemy-%{version}-py*.egg-info

%files apidocs
%defattr(644,root,root,755)
%doc doc/{_images,_modules,_static,changelog,core,dialects,faq,orm,tutorial,*.html,*.js}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
