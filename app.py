import streamlit as st
import openai

# OpenAI APIキーの設定（Secretsから読み取る）
openai_api_key = st.secrets["OPENAI_API_KEY"]["openai_api_key"]
openai.api_key = openai_api_key

# 施設情報の入力フォーム
st.title("施設情報フォーム｜ミニサイト用")

# 入力項目
ota_copy = st.text_input("OTAキャッチコピー", "例.みんなで過ごすから、たのしい。ペット・家族の温泉旅行 応援宿。")
facility_name = st.text_input("施設名", "例.筑後川温泉 ふくせんか")

keyword1 = st.text_area("キャッチコピーキーワード1", "例.貸切風呂の魅力。ふくせんかでは、4つの貸切風呂を完備しており、源泉かけ流しの温泉をプライベートに楽しむことができます。")
keyword2 = st.text_area("キャッチコピーキーワード2", "例.地産地消の料理。地産地消の野菜や果物、新鮮な魚やお肉を使った会席料理。")
keyword3 = st.text_area("キャッチコピーキーワード3", "例.特別室で贅沢な時間。ご家族連れに是非おすすめしたいのが完成したばかりの特別室への宿泊。")

facility_activities1 = st.text_area("館内での過ごし方1", "例.赤ちゃん連れでも安心。赤ちゃんとの旅行を手軽に楽しめるようパパ・ママにうれしいサービスや日用品を無料で提供")
facility_activities2 = st.text_area("館内での過ごし方2", "例.ラウンジ前にはビールサーバー、ジュース、アイスクリームを無料でご用意しております。")
facility_activities3 = st.text_area("館内での過ごし方3", "例.ドッグラン　無料で広々としたドッグランでのびのびリフレッシュ。足洗い場を完備しているので汚れても安心です。")

sightseeing_name1 = st.text_input("周辺エリアの見どころ1：名称", "例.つづら棚田")
sightseeing_desc1 = st.text_area("周辺エリアの見どころ1：説明", "例.美しく積まれた石垣が印象的な棚田です。初秋には金色に輝く稲穂と赤い彼岸花が棚田を彩ります。")
sightseeing_name2 = st.text_input("周辺エリアの見どころ2：名称", "例.やまんどんの果物農園")
sightseeing_desc2 = st.text_area("周辺エリアの見どころ2：説明", "例.7種のいちごや、赤・白・黒系のぶどう、食感の違いを楽しめる梨など果物の品種が豊富な農園です。")
sightseeing_name3 = st.text_input("周辺エリアの見どころ3：名称", "例.浮羽稲荷神社")
sightseeing_desc3 = st.text_area("周辺エリアの見どころ3：説明", "例.山の中腹に建つ神社。赤い鳥居が延々と連なる急な階段が本殿まで続いている。眼下には筑後平野が広がる。")

restaurant_name1 = st.text_input("周辺の人気グルメ1：名称", "例.cafe たねの隣り")
restaurant_desc1 = st.text_area("周辺の人気グルメ1：説明", "例.地元野菜のランチや薬膳カレー、自家製デザート")
restaurant_name2 = st.text_input("周辺の人気グルメ2：名称", "例.うなぎ料理 和食処 松月")
restaurant_desc2 = st.text_area("周辺の人気グルメ2：説明", "例.パリッと焼かれた皮とふわふわの鰻が絶品")
restaurant_name3 = st.text_input("周辺の人気グルメ3：名称", "例.馬庵このみ 吉井本店")
restaurant_desc3 = st.text_area("周辺の人気グルメ3：説明", "例.自家牧場育ちの馬肉が堪能できる専門店")

# 結果の出力
if st.button("生成する"):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """あなたはプロのトラベルライターです。施設紹介文を作成してください。以下のフォーマットに従って、各セクションを分けて出力してください。

『{facility_name}へようこそ！』という文章から始めてください。
OTAキャッチコピー {ota_copy} を考慮に入れて、魅力的なキャッチコピーを {keyword1}、{keyword2}、{keyword3} を基に50文字以内で作成してください。

この宿の魅力を {keyword1}、{keyword2}、{keyword3} を基に、それぞれの特徴を詳しく説明するタイトルと文章を3つ作成してください。タイトルは太字に、文章には名称を含めずに記述してください。

館内での過ごし方の説明には {facility_activities1}、{facility_activities2}、{facility_activities3} を使用し、それぞれの設備やサービスを詳しく説明するタイトルと文章を3つ作成してください。タイトルは太字に。

周辺エリアの見どころには以下を使用：
- {sightseeing_name1}: {sightseeing_desc1}
- {sightseeing_name2}: {sightseeing_desc2}
- {sightseeing_name3}: {sightseeing_desc3}
※各名称をタイトルとし、説明文を作成してください。文章には名称を繰り返さないでください。

周辺の人気グルメには以下を使用：
- {restaurant_name1}: {restaurant_desc1}
- {restaurant_name2}: {restaurant_desc2}
- {restaurant_name3}: {restaurant_desc3}
※各名称をタイトルとし、説明文を作成してください。名称の繰り返しは不要です。

トーンは簡潔で読みやすく、丁寧に。ただし、ウェルカムメッセージにのみ感嘆符を使用してください。"""
            },
            {
                "role": "user",
                "content": f"""
施設名: {facility_name}
キャッチコピー: {ota_copy}
キーワード:
- {keyword1}
- {keyword2}
- {keyword3}
館内での過ごし方:
- {facility_activities1}
- {facility_activities2}
- {facility_activities3}
周辺エリアの見どころ:
- {sightseeing_name1}: {sightseeing_desc1}
- {sightseeing_name2}: {sightseeing_desc2}
- {sightseeing_name3}: {sightseeing_desc3}
周辺の人気グルメ:
- {restaurant_name1}: {restaurant_desc1}
- {restaurant_name2}: {restaurant_desc2}
- {restaurant_name3}: {restaurant_desc3}
"""
            }
        ]
    )

    generated_text = response['choices'][0]['message']['content'].strip()
    st.text(generated_text)
