#=================================================
# 武器屋 Created by Merino
#=================================================
# 場所名
$this_title = '福引所';

# NPC名
$npc_name = '@ﾌｸｽｹ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/lot";

# 背景画像
$bgimg = "$bgimgdir/lot.gif";

# 特別な福引に必要な枚数
$special_lot = 300;


# 100枚以上所持
if ($m{coupon} >= $special_lot) {
	# 必要な福引券数
	$need_coupon = $special_lot;

	my @g_prizes = (90..100);
	my $_g = $g_prizes[ int rand @g_prizes ];
	
	@prizes = (
	# ※番号, 賞品(道具No), 玉の色, 色名, コメント
		[3,		$_g,	"gold",		"ｺﾞｰﾙﾄﾞ",	"！！！えっ！？あれっ！？なんだこれは？！え〜と…ハズレです！………な、なんですか！？…わかりましたよ。他の人には内緒ですよ。",		],
		[15,	60,		"silver",	"ｼﾙﾊﾞｰ",	"おおっ！$ites[60][1]が出ました〜！おめでとうございま〜す！こちらが$ites[60][1]になります！",	],
		[30,	61,		"red",		"ﾚｯﾄﾞ",		"おおっ！$ites[61][1]が出ました〜！おめでとうございま〜す！こちらが$ites[61][1]になります！",	],
		[40,	62,		"blue",		"ﾌﾞﾙｰ",		"おおっ！$ites[62][1]が出ました〜！おめでとうございま〜す！こちらが$ites[62][1]になります！",	],
		[50,	63,		"green",	"ｸﾞﾘｰﾝ",	"おおっ！$ites[63][1]が出ました〜！おめでとうございま〜す！こちらが$ites[63][1]になります！",	],
		[60,	64,		"yellow",	"ｲｴﾛｰ",		"おおっ！$ites[64][1]が出ました〜！おめでとうございま〜す！こちらが$ites[64][1]になります！",	],
		[70,	65,		"purple",	"ﾊﾟｰﾌﾟﾙ",	"おおっ！$ites[65][1]が出ました〜！おめでとうございま〜す！こちらが$ites[65][1]になります！",	],
		[100,	0,		"white",	"ﾎﾜｲﾄ",		"おおっ！ホワイトオーブが出ました〜！って…それはハズレです…",	],
	);
}
else {
	# 必要な福引券数
	$need_coupon = 3;
	
	# 特賞(曜日替わり)
	my @g_prizes = (27,35,36,88,37,38,39);
	my($wday) = (localtime($time))[6];
	
	# 賞品リスト
	# ------------------
	# ※福引の仕組み
	# 0〜999の数字からランダムに１つ選ばれ、当たり番号の数字未満の場合が当たりとなる。
	# 例>   0の数字だった場合→  0以上 1未満なので金の特賞。
	# 例>  24の数字だった場合→ 20以上25未満なので桃の４等(道具No.17)
	# 例> 130の数字だった場合→120以上なのでハズレ
	#-------------------
	@prizes = (
	# ※番号, 賞品(道具No), 玉の色, 色名, コメント
		[1,			$g_prizes[$wday],	"#FFCC33",	"金",	"！！！えっ！？えっ！？お、大当たり〜！大当たり〜！あれ？出ないはずなのにな…ｺﾞﾆｮｺﾞﾆｮ。お、おめでとうございます！特賞です！特賞が出ました〜！どうぞ！こちらが特賞の$ites[ $g_prizes[$wday] ][1]です！お受け取りください！",		],
		[4,			30,					"#FF3333",	"赤",	"！！おっ！大当たり〜！大当たり〜！おめでとうございます！１等が出ました〜！こちらが１等の$ites[30][1]です！",		],
		[8,			33,					"#CC66FF",	"紫",	"！！おっ！大当たり〜！大当たり〜！おめでとうございます！２等が出ました〜！こちらが２等の$ites[33][1]です！",		],
		[14,		23,					"#FFFF00",	"黄",	"大当たり〜！大当たり〜！おめでとうございます！３等が出ました〜！こちらが３等の$ites[23][1]です！",	],
		[20,		16,					"#FF33FF",	"桃",	"おおっ、当たりで〜す！おめでとうございま〜す！４等が出ました〜！こちらが４等の$ites[16][1]です！",	],
		[25,		17,					"#FF33FF",	"桃",,	"おおっ、当たりで〜す！おめでとうございま〜す！４等が出ました〜！こちらが４等の$ites[17][1]です！",	],
		[30,		18,					"#FF33FF",	"桃",,	"おおっ、当たりで〜す！おめでとうございま〜す！４等が出ました〜！こちらが４等の$ites[18][1]です！",	],
		[35,		19,					"#FF33FF",	"桃",	"おおっ、当たりで〜す！おめでとうございま〜す！４等が出ました〜！こちらが４等の$ites[19][1]です！",	],
		[40,		20,					"#FF33FF",	"桃",	"おおっ、当たりで〜す！おめでとうございま〜す！４等が出ました〜！こちらが４等の$ites[20][1]です！",	],
		[45,		21,					"#FF33FF",	"桃",	"おおっ、当たりで〜す！おめでとうございま〜す！４等が出ました〜！こちらが４等の$ites[21][1]です！",	],
		[55,		12,					"#6666FF",	"青",	"当ったり〜！おめでとうございます！５等の$ites[12][1]です！",	],
		[75,		125,				"#33FF33",	"緑",	"おめでとう。６等の$ites[125][1]で〜す！",	],
		[1000,		0,					"#FFFFFF",	"白",	"ハズレです…",	],
	);
}

#=================================================
# ヘッダー表示
#=================================================
sub header_html {
	print qq|<div class="mes">【$this_title】 福引券<b>$m{coupon}</b>枚|;
	print qq| E：$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
}

#=================================================
# はなす言葉
#=================================================
@words = (
	"福引券$need_coupon枚で１回まわすことができるよ",
	"福引の賞品は「＠しょうひん」で確認してね",
	"特賞は曜日によって変わるよ",
	"福引券はルイーダの酒場で食事するともらえるよ",
	"$special_lot枚以上福引券を持っている人は、特別な福引ができるよ",
);

sub shiraberu_npc {
	$mes = "なんと、$mは福引券を見つけた！<br />$npc_name「ダメだよ！あげないよ！」";
}

#=================================================
# 追加アクション
#=================================================
push @actions, ('ふくびき');
push @actions, ('しょうひん');
$actions{'ふくびき'}   = sub{ &fukubiki }; 
$actions{'しょうひん'} = sub{ &shouhin }; 

#=================================================
# ＠ふくびき
#=================================================
sub fukubiki {
	if ($m{coupon} < $need_coupon) {
		$mes = qq|福引券を $need_coupon 枚以上、持っていないようですねぇ…|;
		return;
	}
	
	$m{coupon} -= $need_coupon;
	my $v = int(rand($prizes[-1][0]));
	
	if ($v >= $prizes[-2][0]) {
		my $count = int($m{coupon} / $need_coupon);
		$mes = $need_coupon eq $special_lot ?
			qq|ｶﾞﾗｶﾞﾗｶﾞﾗ…ｺﾛｺﾛｺﾛ…...,,,<font color="$prizes[-1][2]">● 【$prizes[-1][3]ｵｰﾌﾞ】</font> $prizes[-1][4]|:
			qq|ﾌﾟﾆｮﾌﾟﾆｮﾌﾟﾆｮ…ｺﾛｺﾛｺﾛ…...,,,<font color="$prizes[-1][2]">● 【$prizes[-1][3]ｽﾗｲﾑ】</font> $prizes[-1][4]|;
		$mes .= $count > 0 ? qq|あと$count回まわせるよ| : qq|また挑戦してね|;
		return;
	}
	
	for my $i (0 .. $#prizes) {
		if ($v < $prizes[$i][0]) {
			$npc_com .= $need_coupon eq $special_lot ?
				qq|ｶﾞﾗｶﾞﾗｶﾞﾗ…ｺﾛｺﾛｺﾛ…...,,,<font color="$prizes[$i][2]">● 【$prizes[$i][3]ｵｰﾌﾞ】</font>$prizes[$i][4]|:
				qq|ﾌﾟﾆｮﾌﾟﾆｮﾌﾟﾆｮ…ｺﾛｺﾛｺﾛ…...,,,<font color="$prizes[$i][2]">● 【$prizes[$i][3]ｽﾗｲﾑ】</font>$prizes[$i][4]|;
			
			if ($m{ite}) {
				&send_item($m, 3, $prizes[$i][1]);
				$npc_com .= qq|$ites[$prizes[$i][1]][1]は、$mさんの預かり所に送っておきますね|;
			}
			else {
				$npc_com .= qq|はい。どうぞ！|;
				$m{ite} = $prizes[$i][1];
			}
			last;
		}
	}
}

#=================================================
# ＠ふくびき
#=================================================
sub shouhin {
	if ($need_coupon eq $special_lot) {
		$mes = <<"EOM";
	裏福引の賞品リスト
	<table class="table1">
		<tr><td style="color:gold; ">１等</td><td style="color:gold; ">●</td><td>オーブ</td></tr>
	</table>
EOM
	}
	else {
		$mes = <<"EOM";
	福引の賞品リスト
	<table class="table1">
		<tr><td style="color:$prizes[0][2]; ">特賞</td><td style="color:$prizes[0][2]; ">●$prizes[0][3]</td><td>$ites[$prizes[0][1]][1]</td></tr>
		<tr><td style="color:$prizes[1][2]; ">１等</td><td style="color:$prizes[1][2]; ">●$prizes[1][3]</td><td>$ites[$prizes[1][1]][1]</td></tr>
		<tr><td style="color:$prizes[2][2]; ">２等</td><td style="color:$prizes[2][2]; ">●$prizes[2][3]</td><td>$ites[$prizes[2][1]][1]</td></tr>
		<tr><td style="color:$prizes[3][2]; ">３等</td><td style="color:$prizes[3][2]; ">●$prizes[3][3]</td><td>$ites[$prizes[3][1]][1]</td></tr>
		<tr><td style="color:$prizes[4][2]; ">４等</td><td style="color:$prizes[4][2]; ">●$prizes[4][3]</td><td>種系</td></tr>
		<tr><td style="color:$prizes[-3][2];">５等</td><td style="color:$prizes[-3][2];">●$prizes[-3][3]</td><td>$ites[$prizes[-3][1]][1]</td></tr>
		<tr><td style="color:$prizes[-2][2];">６等</td><td style="color:$prizes[-2][2];">●$prizes[-2][3]</td><td>$ites[$prizes[-2][1]][1]</td></tr>
	</table>
EOM
	}
}


1; # 削除不可
