import streamlit as st

# 施設情報の入力フォーム
st.title("施設情報フォーム")

# OTAキャッチコピー
ota_copy = st.text_input("OTAキャッチコピー", "みんなで過ごすから、たのしい。ペット・家族の温泉旅行 応援宿。")

# 施設名
facility_name = st.text_input("施設名", "筑後川温泉 ふくせんか")

# キャッチコピーキーワード
keyword1 = st.text_area("キャッチコピーキーワード1", "ふくせんかでは、4つの貸切風呂を完備しており、源泉かけ流しの温泉をプライベートに楽しむことができます。")
keyword2 = st.text_area("キャッチコピーキーワード2", "地産地消の野菜や果物、新鮮な魚やお肉を使った会席料理。")
keyword3 = st.text_area("キャッチコピーキーワード3", "ご家族連れに是非おすすめしたいのが完成したばかりの特別室への宿泊。")

# 館内での過ごし方
facility_activities1 = st.text_area("館内での過ごし方1", "赤ちゃんとの旅行を手軽に楽しめるようパパ・ママにうれしいサービスや日用品を無料で提供")
facility_activities2 = st.text_area("館内での過ごし方2", "ラウンジ前にはビールサーバー、ジュース、アイスクリームを無料で提供")

# 周辺エリアの見どころ
sightseeing1 = st.text_area("周辺エリアの見どころ1", "美しく積まれた石垣が印象的な棚田です。")
sightseeing2 = st.text_area("周辺エリアの見どころ2", "7種のいちごや、赤・白・黒系のぶどう、食感の違いを楽しめる梨など果物の品種が豊富な農園です。")

# 周辺の人気グルメ
restaurant1 = st.text_area("周辺の人気グルメ1", "地元の旬の野菜を使ったランチや薬膳カレー、和洋の自家製デザート")
restaurant2 = st.text_area("周辺の人気グルメ2", "鰻の焼き加減は皮はパリッと身はフワフワと絶妙な焼き加減")
restaurant3 = st.text_area("周辺の人気グルメ3", "馬肉は、自家牧場にておよそ2年の年月をかけて飼育されたもの")

# 結果の出力
if st.button("生成する"):
    # 結果の生成
    result = f"""
    施設情報

    『{facility_name}へようこそ！』
    {ota_copy}

    この宿の魅力
    **貸切風呂の魅力**
    {keyword1}

    **地産地消の料理**
    {keyword2}

    **特別室で贅沢な時間を**
    {keyword3}

    館内での過ごし方
    **赤ちゃん連れでも安心**
    {facility_activities1}

    **ラウンジでくつろぎのひととき**
    {facility_activities2}

    周辺エリアの見どころ
    **つづら棚田**
    {sightseeing1}

    **やまんどんの果物農園**
    {sightseeing2}

    周辺の人気グルメ
    **cafe たねの隣り**
    {restaurant1}

    **うなぎ料理 和食処 松月(しょうげつ)**
    {restaurant2}

    **馬庵このみ 吉井本店**
    {restaurant3}
    """

    st.text(result)
