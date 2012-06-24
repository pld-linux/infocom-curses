%define		_name		curses
Summary:	Infocom text game - Curses
Summary(pl.UTF-8):   Tekstówka Infocomu - Curses
Name:		infocom-curses
Version:	951024
Release:	2
License:	free
Group:		Applications/Games
Source0:	ftp://ftp.ifarchive.org/if-archive/games/zcode/%{_name}.z5
# Source0-md5:	f06a42a29a5a4e6aa70958c9ae4c37cd
URL:		http://www.ifarchive.org/
Requires:	zcode-wrapper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
As "Curses" opens, you're hunting about in the attic of your family
home, looking for a tatty old map of Paris (you're going on holiday
tomorrow) and generally trying to avoid all the packing. Aunt Jemima
is potting daisies and sulking; the attics are full of endless
distractions and secrets; Greek myths, horoscopes, sixth-century
politics, a less than altogether helpful demon, a mysterious bomb
plot, photography, ritual, poetry and a dream or two all get in your
way; and somehow you keep being reminded of your family through the
ages, and all its Curses...

...could it be that even you are Cursed?

%description -l pl.UTF-8
Gdy "Curses" się zaczyna, grzebiesz na strychu swojego domu
rodzinnego, szukając starego wystrzępionego planu Paryża (jutro
wyjeżdżasz na wakacje) i w zasadzie chcesz uniknąć całego tego
pakowania. Ciocia Jemima hoduje w doniczkach stokrotki i dąsa się;
strych jest pełen niekończących się rozrywek i tajemnic; mity greckie,
horoskopy, polityka VI wieku, zupełnie nieprzydatny demon, tajemniczy
rysunek bomby, fotografie, obrzędy, poezja i marzenie, by wszystko
znalazło się ci na drodze; i w jakiś sposób coś ci przypomina o twojej
rodzinie poprzez wieki i o tych wszystkich przeklęciach...

...czy to możliwe, że nawet ty jesteś przeklęty?

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/zcode}

cp %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/games/zcode
ln -s %{_datadir}/games/zcode/wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/zcode/*.z5
