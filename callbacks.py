import dash, hmm, random
import networkx as nx, plotly.graph_objects as go

@dash.callback(
    [
        dash.Output("transition-graph-store", "data"),
        dash.Output("transition-graph-view", "figure"),
    ],
    [
        dash.Input("create-transition-graph", "n_clicks"),
        dash.State("input-text-area", "value"),
    ],
    prevent_initial_call=True,
)
def update_transition_graph_view(n_clicks, input_text):
    if input_text:
        transition_graph = hmm.create_transition_graph(input_text)

        G = nx.DiGraph()

        for word, next_words in transition_graph.items():
            for next_word, prob in next_words.items():
                G.add_edge(word, next_word, weight=prob)

        pos = nx.spring_layout(G, seed=42)

        edge_x = []
        edge_y = []
        edge_text = []

        for u, v, data in G.edges(data=True):
            x0, y0 = pos[u]
            x1, y1 = pos[v]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
            edge_text.append(f"{u} → {v}: {data['weight']:.2f}")

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=1, color='gray'),
            hoverinfo='text',
            mode='lines')

        node_x = []
        node_y = []
        node_text = []
        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            node_text.append(node)

        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            text=node_text,
            textposition="bottom center",
            hoverinfo='text',
            marker=dict(
                showscale=False,
                color='lightblue',
                size=30,
                line=dict(width=2)
            )
        )

        fig = go.Figure(
            data=[edge_trace, node_trace],
            layout=go.Layout(
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20, l=5, r=5, t=40),
                xaxis=dict(showgrid=False, zeroline=False),
                yaxis=dict(showgrid=False, zeroline=False)
            )
        )

        return transition_graph, fig
    return dash.no_update, dash.no_update

@dash.callback(
    dash.Output("output-text-area", "children"),
    dash.Input("generate-output-text", "n_clicks"),
    dash.State("transition-graph-store", "data"),
)
def generate_output_text(n_clicks, transition_graph):
    if n_clicks and transition_graph:
        start_word = random.choice(list(transition_graph.keys()))
        length = random.randint(10, 20)

        output_text = hmm.generate_sentence(transition_graph, start_word, length)

        return output_text
    return dash.no_update