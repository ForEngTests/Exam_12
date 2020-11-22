import random

print("""よくばり12月考査範囲。
v1.0
""")

J = ["息子の学費を払うために、贅沢品は我慢しています。",
"図書館にいる人の邪魔にならないように、そっと入った。",
"熱中症にならないためには、水分をきちんと補給すること。",
"携帯のバッテリーが切れたので、職員室で充電した。",
"地下にいるから、携帯が圏外になっている。",
"就職して税金も払っているのに、20歳になっていないというだけで、私には投票権がない。",
"若者は以前ほど本を読まなくなったが、だからといって、彼らの好奇心が減少したわけではない。",
"貧困が、多くの子どもたちの就学を阻む最大の要因である。",
"人が晩婚を選択する理由の1つは、自由をできるだけ楽しみたいと思っていることだ。",
"現代人は、忙しくて運動する時間がないためか、太った人が多い。",
"なぜ遅れたの？  霧のため、飛行機が2時間遅れていたんです。",
"私は多くの障害にぶつかったが、友人たちのおかげで何とか乗り越えることができた。",
"私たちは、アンジェラが子ども時代を孤児院で過ごしたのを知って、目頭が熱くなりました。",
"お気に入りのスカートにしみがついたので、落ち込んだ。",
"私たちは甲子園の出場が決まってワクワクした。",
"昨日はとても暑かったので、車のドアで指をやけどした。",
"あなたはまだ結婚するには若すぎるよ。けど、彼氏がお金持ちなら、年は関係ないよ。",
"温泉につかるだけで、日常のストレスがどこかへ吹き飛ぶ。",
"ごめんね。サッカーの試合、録画するの忘れてた。 また？ どうしようもない人だなぁ！",
"デイヴィッドは足を組んで座るのが嫌いだ。足が痺れるからだ。",
"今日、おろしたてのヒールをはいてウィンドウショッピングをしたら、足にまめができた。",
"ケビンは、片手にビール、もう一方の手にスポーツ新聞を持って、パブに1人で立っていた。",
"夜間、ライトをつけないで自転車に乗るのは、愚かで危険なことだ。",
"電車で隣に座った酔っ払いの男が眠りこけて、私の肩にもたれかかった。",
"足首が腫れているよ。どうしたの？ サッカーをしていて捻挫したんだ。",
"ティムは突然興奮して、クマのぬいぐるみを箱から取り出した。",
"治安の問題を考慮すれば、留学は米国よりオーストラリアの方がいいように思われる。",
"英単語の一覧を丸暗記するのは、信じられないくらい疲れる。 本当そうだよね。やってられないよ。",
"趣味はホームセンター巡りです。 会社の近くに一軒新しいのができたの知ってる？",
"近頃は韓国語ブームね。 うん、うちの母でさえはまってるよ。",
"ユーチューブで動画を見ていて、気がつけば、3時間も経っていた。",
"マザー・テレサは修道女として、貧しい人々の救済に一生を捧げた。",
"自衛隊に関するこの記事は、読んでみる価値が十分にある。",
"渋滞していたため、会社に定時に到着できず、上司に叱られた。",
"胃の調子が悪くて吐き気がする。 動かないで。バケツ持ってきてあげるから。",
"80歳になる祖母は、毎日近所のプールに泳ぎに出かける。",
"4月の初めごろ、日本ではたくさんの人がお花見に出かける。",
"これをギフト用に包んでもらいたいのですが。 かしこまりました。",
"素面なら、遅く帰ってきても構わないよ。",
"最初はコンタクトがなかなかうまく入らないものだよ。",
"私は低血圧だけど、朝は大丈夫だ。",
"経済的な理由で、留学をあきらめねばならなかった。",
"ピーターは京都に数ヶ月住んでいるが、まだ交通機関に慣れていない。",
"カレンは健康のために、エレベーターではなく階段を使っている。",
"明日は晴れるかな？  大丈夫。エリザベスをビアガーデンに連れて行ったら？",
"自分の価値観だけが絶対だと思うのは危険です。",
"この国がたった1つのエネルギー源に頼るのは危険だ。",
"他人に迎合するためだけに自分の信念を曲げるのは、あさましいことだ。",
"プールでゆっくり日光浴をするのは、本当にいいね。",
"香港出張を来週に延期することは、可能でしょうか？",
"定年を70歳に引き上げることは、誰にとっても有益であろう。",
"君がこのレストランの予約をずいぶん前にしておいたのは、賢明だった。",
"集中力と明晰な思考力を養うには、よく眠るのが一番だ。",
"日本の宴会では、人に飲み物をつぐのが礼儀です。",
"ナオミは買い物中毒と言ってもおかしくはない。",
"このウールのカーディガンは、手洗いするよりクリーニング店に持って行った方がよい。",
"今日は洗車日和だ。エマ、ホース持って来いよ。  わかった。いい考えね。",
"今日は君が皿洗いをする番だ。僕は昨日したからね。",
"客を招いたら、家のすべての部屋を案内してまわるのが欧米の通例である。",
"ウッドハムがボスだ。その会を開くかどうかを決めるのは彼だ。",
"まともな歩道を取り払い、それを舗装し直すのは、税金の無駄遣いである。",
"公共の場所でのきちんとした行動の仕方を子どもに教えるのは、親の義務だ。",
"ケニーはいくら飲んでも平気だ。二日酔いしない。",
"英語を話せさえすれば国際人になれると勘違いしている人がまだ大勢いるのは、残念だ。",
"父はとても頑固だから、考えを変えるように説得するのは無駄だと思う。",
"私たちは町がクリスマス前に雪景色となったのは、10年ぶりのことだった。",
"外国に行って初めて、日本の伝統文化の良さに気付く。",
"ハリケーンの動きを正確に予測できるようになるには、まだ多くの年月を要するだろう。",
"休憩してから交渉を続けましょう。  いい考えですね。",
"事務所は、5階でエレベーターを降りてすぐです。",
"いったん鍋をコンロから下ろしたら、そのまま5分間蒸らしてください。",
"中国に旅行するたびに、もっと熱心に中国語の勉強をしておけばよかったと後悔する。"]

E = ["We do without luxuries in order to pay for our son's school expenses.",
"I went into the library quietly so that I would not disturb the people there.",
"To avoid heatstroke, make sure you drink plenty of fluids.",
"My cell phone's batteries were dead, so I recharged them at the staff room.",
"I can't get a signal on my cell phone because I'm in the basement.",
"I have a job and pay taxes, but I do not have the right to vote simply because I am under twenty.",
"Just because young people read less, this does not mean that they are less curious.",
"Many children cannot go to school mainly because their families are poor.",
"People choose to marry late partly because they want to enjoy their freedom as long as possible.",
"Many people today are overweight probably because they are too busy to exercise.",
"Why are you late? The plane was delayed for two hours because of fog.",
"I had a lot of problems, but thanks to my friends, I managed to overcome them.",
"We were all moved to learn that Angela had spent her childhood in an orphanage.",
"I was disappointed that my favorite skirt had gotten stained.",
"We were thrilled that we had made it through to the National High-School Baseball Tournament.",
"Yesterday, it was so hot that I burned my fingers on the car door.",
"You're not old enough to get married. But I guess if your boyfriend's rich, age doesn't matter.",
"Soaking in a bath at a hot spring resort is enough to relieve all the stress of everyday life.",
"Sorry, I forgot to record the soccer game. Again? You're hopeless!",
"David hates sitting with his legs crossed. His legs go to sleep.",
"I went window shopping with brand-new high heels on today and got blisters on my feet.",
"Kevin was standing alone in a pub with a glass of beer in one hand and a sports paper in the other.",
"Riding a bicycle at night without the light on is stupid and dangerous.",
"The drunken man sitting next to me on the train fell asleep, resting his head on my shoulder.",
"Your ankle is swollen. What happened? I sprained it while playing soccer.",
"Suddenly excited, Tim took the teddy bear out of the box.",
"Considering the issue of street crime, it seems better to study in Australia than in the U.S.",
"Memorizing lists of English words is incredibly tiring! I agree. I've had enough.",
"In my free time, I like going to DIY stores. Do you know about the new one near the office?",
"Studying Korean is very popular nowadays. Yes, even my mother's into it.",
"I had spent three hours watching videos on YouTube before realizing it.",
"Mother Teresa, as a nun, devoted all her life to giving a helping hand to poor people.",
"This article on the Self-Defense Forces is well worth reading.",
"The heavy traffic prevented me from arriving on time, so my boss got upset.",
"I have an upset stomach and feel like throwing up. Don't move. I'll get you a bucket.",
"My grandmother, who is eighty, goes swimming at a local pool every day.",
"In Japan, crowds of people go cherry-blossom viewing around the beginning of April.",
"Would you mind gift-wrapping this for me, please? Certainly not, ma'am.",
"I don't mind your coming home late as long as you're sober.",
"People have difficulty putting in contact lenses at first.",
"I have low blood pressure, but I have no difficulty getting up early.",
"For financial reasons, I had to give up the idea of studying abroad.",
"Peter has lived in Kyoto for months, but he is still not used to the public transportation.",
"In order to stay healthy, Karen walks up the stairs, instead of taking the elevator.",
"Will it be a sunny day tomorrow? Yes. Why don't you take Elizabeth to a beer garden?",
"It is dangerous to think that your values are the only correct ones.",
"It would be dangerous for this country to depend on only one energy source.",
"It is shameful to change your opinions simply to please other people.",
"It is really nice to have time to sunbathe at the pool.",
"Is it possible for you to postpone our business trip to Hong Kong until next week?",
"It will be beneficial for everyone if the standard retirement age is raised to seventy.",
"It was wise of you to make a reservation at this restaurant so far in advance.",
"In order to develop your ability to concentrate and think clearly, it is best to get enough sleep.",
"In Japan, it is good manners to pour other people's drinks at parties.",
"It is no exaggeration to say that Naomi is addicted to shopping.",
"It's better to take this wool cardigan to the dry cleaner than to wash it by hand.",
"It's a good day to wash the car. Emma, go and get the hose! OK. Good idea.",
"It's your turn to do the dishes today. I did them yesterday.",
"It is not unusual in the West to show guests around your whole house.",
"Mr. Woodham is the boss. It's up to him to organize the meeting.",
"It is a waste of taxpayers' money to tear up decent sidewalks and then repave them.",
"It is the responsibility of parents to teach their children how to behave properly in public.",
"It does not matter how much Kenny drinks, because he never gets hungover.",
"It is a pity that many people still mistakenly believe that they have only to speak English to be internationally-minded.",
"My father is very stubborn, so it is no use trying to persuade him to change his mind.",
"It was for the first time in ten years that we saw our town covered with snow before Christmas.",
"It is not until you go abroad that you realize how wonderful traditional Japanese culture is.",
"It will be many years before anyone can accurately predict a hurricane's behavior.",
"Let's take a break before we continue the negotiations. That sounds like a good idea.",
"You'll see the office as soon as you get off the elevator on the fifth floor.",
"Once you take the pot off the stove, let it stand for five minutes.",
"Every time I travel to China, I regret that I did not study Chinese harder."]

Qnum = int(input("問題数?: "))

num = [i for i in range(len(E))]
random.shuffle(num)

wrong_list = []
score = 0

for i in range(Qnum):
 print(i + 1)
 print(J[num[i]])
 ans = input()
 if ans == E[num[i]]:
  print("Correct.")
  score += 1
 else:
 	print("Wrong.")
 	print("Ans:", E[num[i]])
 	wrong_list.append(num[i] + 213)
 print()
 print()

wrong_list.sort()

print("RESULT:")
print(score, "/", Qnum)
print(wrong_list)
if score == Qnum:
 print("Perfect!")
