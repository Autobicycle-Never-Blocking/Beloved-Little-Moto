
from collections import defaultdict
import networkx as nx




position_names = lagou_df['positionName'].tolist()
skill_lables = lagou_df['skillLables'].tolist()
skill_position_graph = defaultdict(list)
for p, s in zip(position_names, skill_lables):
    skill_position_graph[p] += eval(s)


G = nx.Graph(skill_position_graph)

pr = nx.pagerank(G, alpha=0.9)
ranked_position_and_ability = sorted([(name, value) for name, value in pr.items()],
                                     key=lambda x: x[1],
                                     reverse=True)
ranked_position_and_ability
