'''
    This model is used to query the DB related to all the sensor data, this model is not meant
    to add data from the ESP32 to the database, thats done in the utils/mqtt/, where the script 
    subscribes to the topics where all the data is being dumped, its there where the data is being
    orginized and stored in the database.
    
    This model is going to be used to query to feed the history or other data realted things that dont
    need live values.
'''    