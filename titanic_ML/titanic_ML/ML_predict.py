def prediction_model(pcclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    x = [[pcclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest = pickle.load(open('titanic_model.sav','rb'))
    prediction = randomforest.predict(x)
    return(prediction)
