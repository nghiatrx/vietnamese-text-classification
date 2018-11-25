# congnghe - tech: 0, 
# suckhoe - health: 1, 
# thethao - sport: 2, 
# xe - car & motor: 3

from tensorflow.python.keras import models
import pickle

vectorizer = pickle.load(open("./model/vectorizer.pickle", "rb"))
selector = pickle.load(open("./model/selector.pickle", "rb"))

text = """TP.HCM cảnh báo ngộ độc thực phẩm do vi khẩn tụ cầu vàng
        'Thực phẩm giàu chất đạm, chất béo, thực phẩm có hàm lượng nước cao, nhiều tinh bột và nhiệt độ bảo quản thực phẩm không đảm bảo dễ bị nhiễm tụ cầu vàng.
        Ngày 23.11, Ban Quản lý An toàn thực phẩm (ATTP) TP.HCM đã có cảnh báo về tình trạng ngộ độc thực phẩm (NĐTP) trên địa bàn TP, đặc biệt là ngộ độc do vi sinh vật, trong đó có vi khuẩn tụ cầu vàng.
        Theo thống kê của Ban Quản lý ATTP, từ năm 2010 đến tháng 11.2018, trên địa bàn TP đã xảy ra 54 vụ NĐTP. Trong đó, ngộ độc do thực phẩm bị nhiễm vi sinh vật là 33 vụ (chiếm 61%), do độc tố 14 vụ (chiếm 26%), do hóa chất 2 vụ (chiếm 4%), không xác định được nguyên nhân 2 vụ (4%). Trong số vụ NĐTP do vi sinh vật, ngộ độc do tụ cầu vàng (Staphylococcus aureus) 14 vụ (chiếm 42%)."""


x_val = vectorizer.transform([text])
x_val = selector.transform(x_val).astype('float32')

new_model = models.load_model('./model/MyModel.h5')

a = new_model.predict(x_val)

print(a)
