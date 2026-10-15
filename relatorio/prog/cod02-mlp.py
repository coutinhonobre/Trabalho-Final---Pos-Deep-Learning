class MLP(nn.Module):
    def __init__(self, n_in, n_out, hidden_units, dropout=0.0, batch_norm=False):
        super().__init__()
        layers, prev = [], n_in
        for h in hidden_units:                       # camadas ocultas
            layers += [nn.Linear(prev, h)] + ([nn.BatchNorm1d(h)] if batch_norm else []) \
                      + [nn.ReLU(), nn.Dropout(dropout)]
            prev = h
        layers.append(nn.Linear(prev, n_out))        # saída: 1 logit por classe
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x)
