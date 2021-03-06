#=================================================
# 道具屋 Created by Merino
#=================================================
# 場所名
$this_title = '道具屋';

# NPC名
$npc_name = '@ｱｲﾃﾑｺ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/item";

# 背景画像
$bgimg = "$bgimgdir/item.gif";

# 売っている道具(No)
@sales = $m{job_lv} >= 7 ? (1,2,3,7,8,9,11,76,14,79,102,41,42,101,127)
	   : $m{job_lv} >= 5 ? (1,2,3,7,8,9,11,76,14,79,41,42,101,127)
	   : $m{job_lv} >= 3 ? (1,2,7,8,9,11,14,79,41,42,127)
	   : $m{job_lv} >= 1 ? (1,2,7,8,9,11,14,79,127)
	   :                   (1,7,8,9,127)
	   ;



#=================================================
# はなす言葉
#=================================================
@words = (
	"いらしゃいませぇ〜ここは$this_titleニャ",
	"冒険に出る前に道具があると便利ニャ",
	"初心者たんには薬草をオススメしてますぅ",
	"守りの石は相手からのだめぇじを軽減することができるらしいニャ",
	"$mたんは顔色が悪そうなのでぇ、毒消し草を食べるといいニャ",
	"この草おいしいニャ。モグモグ…。あぅっ！またお店の品を食べてしまったニャ…",
	"天使の鈴は頭が悪い人に使うといいらしぃニャ。あたしのことぢゃないニャ",
	"$mたんの今日の夕食は薬草料理がオススメニャ",
	"$mたんはべじたりあんですかぁ？",
	"魔法使いたんは魔法の聖水を持っていくとよいですよぉ",
	"この世界のどこかに秘密の店というあやしいお店があるらしいですよぉ",
	"今日のオススメ商品はコレニャ！じゃじゃ〜ん <b>$ites[$sales[int(rand(@sales))]][1]</b> ニャ！",
);

#=================================================
# ＠しらべる>NPC
#=================================================
sub shiraberu_npc {
	$mes = qq|<span onclick="text_set('＠ひみつのみせ に行きたい')">$npc_name「ほえ？なんでしょうかぁ？」</span>|;
}

#=================================================
# 追加アクション
#=================================================
push @actions, ('かう', 'うる');
$actions{'かう'} = sub{ &kau };
$actions{'うる'} = sub{ &uru };
$actions{'ひみつのみせ'} = sub{ &himitsunomise };

#=================================================
# ＠ひみつのみせ
#=================================================
sub himitsunomise {
	return if $m{job_lv} < 7;
	$mes = "秘密の店を見つけました！";
	$m{lib} = 'secret';
	&auto_reload;
}

#=================================================
# ＠かう
#=================================================
sub kau {
	my $target = shift;
	
	my $h_no = &get_helper_item(3);

	my $p = qq|<table class="table1"><tr><th>名前</th><th>値段</th></tr>|;
	for my $i (@sales) {
		next if $h_no =~ /,$i,/; # 手助けクエストで依頼されているアイテムは除く
		$ites[$i][2] *= 2; # 錬金できるので２倍
		if ($ites[$i][1] eq $target) {
			if ($m{money} >= $ites[$i][2]) {
				if ($m{ite}) {
					&send_item($m, 3, $i);
					$npc_com = "$ites[$i][1]は$mニャンの預かり所の方に投げましたニャ！";
				}
				else {
					$m{ite} = $i;
					$npc_com = "$ites[$i][1]ですね。はい、どうぞ！";
					require "./lib/_add_collection.cgi";
					&add_collection;
				}
				$m{money} -= $ites[$i][2];
			}
			else {
				$mes = "ビンボーにゃの？働かにゃいの？";
			}
			return;
		}
		$p .= qq|<tr onclick="text_set('＠かう>$ites[$i][1] ')"><td>$ites[$i][1]</td><td align="right">$ites[$i][2] G</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|どれを買うニョ？<br />$p|;
	$act_time = 0;
}

#=================================================
# ＠うる
#=================================================
sub uru {
	my $target = shift;
	
	unless ($m{ite}) {
		$mes = "何を売るニョ？何も道具を持っていないニョ";
		return;
	}
	
	# 買取金額
	my $buy_price = int($ites[$m{ite}][2] * 0.5);
	
	if ($ites[$m{ite}][1] eq $target) {
		$npc_com = "$buy_price Gで $ites[$m{ite}][1] を買い取りまちた";
		$m{money} += $buy_price;
		$m{ite} = 0;
		return;
	}

	$mes = qq|<span onclick="text_set('＠うる>$ites[$m{ite}][1] ')">$ites[$m{ite}][1]なら $buy_price Gで買うニャ！</span>|;
	$act_time = 0;
}


1; # 削除不可
