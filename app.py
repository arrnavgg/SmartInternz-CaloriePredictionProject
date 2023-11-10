# app.py

from flask import Flask, render_template
import sqlite3
import plotly.graph_objs as go
import plotly.offline as opy

app = Flask(__name__)

def fetch_user_name(userid):
    conn = sqlite3.connect('Calorie.db')
    cursor = conn.cursor()

    user_query = "SELECT name FROM users WHERE userid = ?"
    cursor.execute(user_query, (userid,))
    user_data = cursor.fetchone()

    cursor.close()
    conn.close()

    return user_data[0] if user_data else None

# Function to query data from the SQLite database
def fetch_data(userid):
    conn = sqlite3.connect('Calorie.db')
    cursor = conn.cursor()

    # Example query: Retrieve total quantity sold for each product
    query = "SELECT exercise_name, duration FROM exercise WHERE userid = ?"
    cursor.execute(query, (userid,))
    data = cursor.fetchall()

    # Example query: Retrieve total quantity sold over time
    time_query = "SELECT date, calories FROM exercise WHERE userid = ?"
    cursor.execute(time_query, (userid,))
    time_data = cursor.fetchall()

    calories_query = "SELECT exercise_name, calories FROM exercise WHERE userid = ?"
    cursor.execute(calories_query, (userid,))
    calories_data = cursor.fetchall()

    heart_query = "SELECT bpm, calories FROM exercise WHERE userid = ?"
    cursor.execute(heart_query, (userid,))
    heart_data = cursor.fetchall()


    cursor.close()
    conn.close()

    return data, time_data, calories_data, heart_data


# Function to create a Plotly bar chart
def create_bar_chart(data):
    exercise, duration = zip(*data)

    trace = go.Bar(x=exercise, y=duration)
    layout = go.Layout(title='Exercise vs duration', xaxis=dict(title='Exercise'), yaxis=dict(title='Duration'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')


def create_line_chart(time_data):
    date, calories = zip(*time_data)

    trace = go.Scatter(x=date, y=calories, mode='lines+markers', marker=dict(size=10), line=dict(width=2))
    layout = go.Layout(title='Total Calories Over Time', xaxis=dict(title='Date'), yaxis=dict(title='Total Calories'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div') 

def create_pie_chart(data, title):
    exercise_names, calories = zip(*data)

    trace = go.Pie(labels=exercise_names, values=calories)
    layout = go.Layout(title=title)
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')

def create_heart_rate_scatter_plot(data):
    bpm, calories = zip(*data)

    trace = go.Scatter(x=bpm, y=calories, mode='markers', marker=dict(size=12))
    layout = go.Layout(title='Heart Rate vs. Calories Burned', xaxis=dict(title='Heart Rate (BPM)'), yaxis=dict(title='Calories Burned'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')


@app.route('/<int:userid>')
def user_dashboard(userid):
    user_name = fetch_user_name(userid)

    if user_name:
        exercise_data, time_data, calories_data, heart_data = fetch_data(userid)

        bar_chart = create_bar_chart(exercise_data)
        line_chart = create_line_chart(time_data)
        pie_chart = create_pie_chart(calories_data, title='Exercise Distribution and Calories Burned')
        scatter_plot = create_heart_rate_scatter_plot(heart_data)


        return render_template('user_dashboard.html',
                               username=user_name,
                               bar_chart=bar_chart,
                               line_chart=line_chart,
                               pie_chart=pie_chart,
                               scatter_plot=scatter_plot
                            )
    else:   
        return "User not found"

if __name__ == '__main__':
    app.run(debug=True)
