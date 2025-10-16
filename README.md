# LangChain ve LangGraph kullanarak retrieval augmented generation (RAG) sistemi

<img width="1423" height="746" alt="adaptıveRAG" src="https://github.com/user-attachments/assets/a69b9dd3-52b8-43bb-aaea-3a2c2a64d6ef" />

## Bu projedeki Graph; kullanıcının sorusu, alınan belgeler ve oluşturulan cevap gibi mevcut duruma göre bilgi akışını ve karar verme sürecini yönetir.
  
1) Route Question: Sistem önce kullanıcının sorusunu analiz ederek en uygun ilk veri kaynağını belirler. Soruyu vector database'ine ya da web search'e yönlendirir.
2) Retrieve: Vector database'e yönlendirilirse, sistem ChromaDB'den ilgili belgeleri geri getirir.
3) Grade Documents:Alınan her belge, soru ile alaka düzeyine göre derecelendirilir. Herhangi bir belge alakasız olarak değerlendirilirse, documents'ın içine alınmaz. Alakalı olanlarla sonuç üretilir. Eğer tüm belgeler alakasızsa web search'e geçilir
4) Hallucination Check:  Cevap, sağlanan belgelerdeki gerçeklere dayalı olduğundan emin olmak için kontrol edilir.
5) Final Decision: Oluşturma gerçeklere dayalı ve alakalı ise, süreç sona erer ve cevap döndürülür.


### Soru: How can i make hamburger
<img width="1112" height="441" alt="AdvanceRAGWebSearch" src="https://github.com/user-attachments/assets/24dabff4-0ff0-4ed3-9bc7-f728a923329f" />

### Soru: What is Maximum Inner Product Search (Verilen dosyalar ile alakalı)
<img width="1111" height="442" alt="AdvcanceRAGDocumentSearch" src="https://github.com/user-attachments/assets/664c137e-5343-490c-b7d2-d8495c3c7454" />
