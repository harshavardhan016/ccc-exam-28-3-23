
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'coolGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts UNWEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#

def coolGraph(g_nodes, g_from, g_to):
    # Write your code here
    {
    int ans = 0;
    int n = related.size();
    vector<vector<int>> graph(n,vector<int>(n,0));
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            
            if (related[i][j] == '1')   
            {
                graph[i][j]=1;
            }
        }
    }

    vector<int> visit(n, 0);
    for (int i = 0; i < n; ++i)
    {
        if (!visit[i])
            dfs(graph, i, visit), ans++;
    }
    return ans;
}

if name == 'main':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i] = map(int, input().rstrip().split())

    result = coolGraph(g_nodes, g_from, g_to)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()