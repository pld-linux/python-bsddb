
%include /usr/lib/rpm/macros.python
%define	pname	bsddb3

Summary:	Python interface for BerkeleyDB 3.1 and 3.2
Summary(pl):	Interfejs Pythona do BerkeleyDB 3.1 i 3.2
Name:		python-bsddb3
Version:	3.4.0
Release:	1
License:	UNKNOWN
Vendor:		Robin Dunn <robin@alldunn.com>
Group:		Development/Languages/Python
Source0:	http://prdownloads.sf.net/pybsddb/%{pname}-%{version}.tar.gz
Patch0:		%{name}-db4.patch
URL:		http://PyBSDDB.sourceforge.net/
Obsoletes:	bsddb3
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
BuildRequires:	db4-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a nearly complete wrapping of the Sleepycat C API
for the Database Environment, Database, Cursor, and Transaction
objects, and each of these is exposed as a Python Type in the
bsddb3.db module. The databse objects can use various access methods:
btree, hash, recno, and queue. For the first time all of these are
fully supported in the Python wrappers. Please see the documents in
the docs directory of the source distribution or at the website for
more details on the types and methods provided.

%description -l pl
Ten modu³ dostarcza prawie ca³kowite opakowanie API C Sleepycat do
obiektów ¶rodowiska baz danych, baz danych, kursorów i transakcji, z
których ka¿dy jest udostêpniony jako pythonowy typ w module bsddb3.db.
Obiekty bazy danych mog± u¿ywaæ ró¿nych metod dostêpu: btree, hash,
recno i queue. Jest to pierwsza implementacja obs³ugi tych obiektów
dla Pythona. Wiêcej szczegó³ów o typach i metodach znajduje siê w
za³±czonej dokumentacji lub na stronie WWW.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install --root=$RPM_BUILD_ROOT --optimize=2

# shutup check-files
rm -f $RPM_BUILD_ROOT/%{py_sitedir}/bsddb3/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.txt docs/ README.txt
%dir %{py_sitedir}/bsddb3
%{py_sitedir}/bsddb3/*.py?
%attr(755,root,root) %{py_sitedir}/bsddb3/*.so
