# 2️⃣ Pie chart summary
# pos = sum(1 for s in compound_scores if s > 0)
# neu = sum(1 for s in compound_scores if s == 0)
# neg = sum(1 for s in compound_scores if s < 0)
# plt.figure(figsize=(6, 6))
# plt.pie([pos, neu, neg], labels=['Positive','Neutral','Negative'], autopct='%1.1f%%', startangle=90)
# plt.title("Overall Sentiment Distribution")
# plt.tight_layout()
# plt.show()