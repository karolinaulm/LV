import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

plt.figure(figsize=(10, 4))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.title(y_train[i])
    plt.axis("off")
plt.show()


x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)


model=keras.Sequential()
model.add(layers.Dense(units=128,activation='relu'))
model.add(layers.Dense(units=10,activation='softmax'))

model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train_s,y_train_s,epochs=5,batch_size=32)

train_loss, train_acc = model.evaluate(x_train_s, y_train_s, verbose=0)
test_loss, test_acc = model.evaluate(x_test_s, y_test_s, verbose=0)

print("Točnost na train skupu:", train_acc)
print("Točnost na test skupu", test_acc)

y_pred = model.predict(x_test_s)
y_pred = np.argmax(y_pred, axis=1)

cm = confusion_matrix(y_test, y_pred)
print("Matrica zabune:")
print(cm)

wrong = np.where(y_pred != y_test)[0]

plt.figure(figsize=(10, 6))
for i in range(10):
    idx = wrong[i]
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[idx].reshape(28, 28), cmap="gray")
    plt.title("Točno:" + str(y_test[idx]) + " \nPogrešno:" + str(y_pred[idx]))
    plt.axis("off")
plt.show()
