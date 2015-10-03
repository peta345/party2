#!/usr/local/bin/perl
require 'config.cgi';
require './lib/_data.cgi';
#================================================
# Memory Created by Merino
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	my $name = pack 'H*', $in{id};
	&error("�v���C���[$name�����݂��܂���") unless -f "$userdir/$in{id}/memory.cgi";
	
	my %pars = &collection_pars;
	print qq|<form action="$htmldir/player_list.html"><input type="submit" value="�v���C���[�ꗗ�ɖ߂�" /></form>|;
	print qq|<h2>$name�̋O��</h2>|;
	print qq|<form action="profile.cgi" target="_blank"><input type="hidden" name="name" value="$name" /><input type="submit" value="$name�̃v���t�B�[��" /></form>| if -s "$userdir/$in{id}/profile.cgi";;
	print qq|<form action="$userdir/$in{id}/monster_book.html" target="_blank"><input type="submit" value="$name�̃����X�^�[�u�b�N" /></form>|;
	print qq|<table class="table1">|;
	print qq|<tr><td>����R���v���[�g���s<b>$pars{1}</b>���t</td></tr>|;
	print qq|<tr><td>�h��R���v���[�g���s<b>$pars{2}</b>���t</td></tr>|;
	print qq|<tr><td>����R���v���[�g���s<b>$pars{3}</b>���t</td></tr>|;
	print qq|</table>|;
	
	open my $fh, "< $userdir/$in{id}/memory.cgi" or &error("$userdir/$in{id}/memory.cgi�t�@�C�����ǂݍ��߂܂���");
	print qq|<li>$_</li><hr size="1" />\n| while <$fh>;
	close $fh;
}

sub collection_pars {
	my %pars = ();
	my $kind = 1;
	open my $fh, "< $userdir/$in{id}/collection.cgi" or &error("$userdir/$in{id}/collection.cgi�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		$line =~ tr/\x0D\x0A//d;
		my @nos = split /,/, $line;
		pop @nos; # �擪�̋������
		
		if (@nos <= 0) {
			$pars{$kind} = 0;
		}
		elsif ($kind eq '1') {
			$pars{$kind} = int(@nos / $#weas * 100);
		}
		elsif ($kind eq '2') {
			$pars{$kind} = int(@nos / $#arms * 100);
		}
		elsif ($kind eq '3') {
			$pars{$kind} = int(@nos / $#ites * 100);
		}
		$pars{$kind} = 100 if $pars{$kind} > 100;
		++$kind;
	}
	close $fh;
	
	return %pars;
}