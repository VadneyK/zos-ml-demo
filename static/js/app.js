function App() {
    const [transaction, setTransaction] = React.useState({
        amount: '',
        time_of_day: '',
        transaction_type: '1',
        transaction_id: ''
    });
    const [result, setResult] = React.useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:5000/api/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(transaction),
            });
            const data = await response.json();
            setResult(data);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const handleChange = (e) => {
        setTransaction({
            ...transaction,
            [e.target.name]: e.target.value
        });
    };

    return (
        <div className="container mt-5">
            <h1 className="mb-4">z/OS Transaction Analyzer</h1>
            <div className="row">
                <div className="col-md-6">
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label className="form-label">Transaction Amount</label>
                            <input
                                type="number"
                                className="form-control"
                                name="amount"
                                value={transaction.amount}
                                onChange={handleChange}
                                required
                            />
                        </div>
                        <div className="mb-3">
                            <label className="form-label">Time of Day (24h format)</label>
                            <input
                                type="number"
                                className="form-control"
                                name="time_of_day"
                                value={transaction.time_of_day}
                                onChange={handleChange}
                                min="0"
                                max="23"
                                required
                            />
                        </div>
                        <div className="mb-3">
                            <label className="form-label">Transaction Type</label>
                            <select
                                className="form-control"
                                name="transaction_type"
                                value={transaction.transaction_type}
                                onChange={handleChange}
                            >
                                <option value="1">Regular Transfer</option>
                                <option value="2">Large Transfer</option>
                                <option value="3">International Transfer</option>
                            </select>
                        </div>
                        <div className="mb-3">
                            <label className="form-label">Transaction ID</label>
                            <input
                                type="text"
                                className="form-control"
                                name="transaction_id"
                                value={transaction.transaction_id}
                                onChange={handleChange}
                            />
                        </div>
                        <button type="submit" className="btn btn-primary">Analyze Transaction</button>
                    </form>
                </div>
                <div className="col-md-6">
                    {result && (
                        <div className={`alert ${result.is_normal ? 'alert-success' : 'alert-danger'}`}>
                            <h4>Analysis Result</h4>
                            <p>Transaction ID: {result.transaction_id}</p>
                            <p>Status: {result.is_normal ? 'Normal' : 'Anomalous'}</p>
                            <p>Risk Score: {(result.risk_score * 100).toFixed(2)}%</p>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));
