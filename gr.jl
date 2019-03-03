using JSON
using Plots

cd(@__DIR__)

function graphplot()
    pl=plot()
    data = JSON.parsefile("./Backend/db/health-history.json")
    d = data["1"]["health"]
    k = collect(keys(d))
    r = (e) -> parse(Float64, e)
    val = d["power_out_p1"]
    a = r.(collect(keys(val)))
    b = r.(collect(values(val)))
    @show a
    scatter!(pl, a, b)
    plot!(pl, a, b)
    pl
end

graphplot()

function graphplay()
    display(graphplot())
    sleep(0.4)
    graphplay()
end

graphplay()
