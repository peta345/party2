# Ýè
%k = (
	p_name		=> '@ßÆ±@',			# NGXg¼
	p_join		=> 4,					# í¬QÁãÀ(l)
	p_leader	=> $leader,				# NGXg[_[¼
	speed		=> 12,					# isXs[h(b)
	need_join	=> 'hp_200_o',			# QÁð(./lib/quest.cgi 192sÚ ½èðQl)
);


# óííi(¹ïNo)
@treasures = (
[], # íNo
[], # hïNo
[59..65,107,107], # ¹ïNo
);

# bosses
@bosses = ();
for my $name (@partys) {
	push @bosses, {
		name		=> $name,
		hp			=> $ms{$name}{mhp} * 50,
		mp			=> $ms{$name}{mmp} * 50,
		at			=> $ms{$name}{at} * 2,
		df			=> $ms{$name}{df} * 2,
		ag			=> $ms{$name}{ag} * 2,
		get_exp		=> $ms{$name}{get_exp} * 30,
		get_money	=> $ms{$name}{get_money} * 30,
		icon		=> $ms{$name}{icon},

		job			=> $ms{$name}{job},
		sp			=> $ms{$name}{sp},
		old_job		=> $ms{$name}{old_job},
		old_sp		=> $ms{$name}{old_sp},
		tmp			=> 'åhä',
	}
}




1;
