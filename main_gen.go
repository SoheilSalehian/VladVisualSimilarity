// *********************************************************************
// PARTIALLY GENERATED FILE -- DO NOT EDIT unless custom instrumentation
// Parameterized with:
//
// EndpointName = index
// RequestName = dataPath
// RequestType = string
// ResponseName = status
// ResponseType = string
// *********************************************************************

package main

import (
	"fmt"
	"net/http"
	"os"
	"time"

	"github.com/go-kit/kit/log"
	"github.com/go-kit/kit/metrics"
	kitprometheus "github.com/go-kit/kit/metrics/prometheus"
	httptransport "github.com/go-kit/kit/transport/http"
	stdprometheus "github.com/prometheus/client_golang/prometheus"
	"golang.org/x/net/context"
)

func main() {
	ctx := context.Background()

	// Setup logging
	logger := log.NewLogfmtLogger(os.Stderr)

	// Setup instrumentation
	fieldKeys := []string{"method", "error"}
	requestCount := kitprometheus.NewCounter(stdprometheus.CounterOpts{
		Namespace: "indexGroup",
		Subsystem: "VLAD",
		Name:      "requestCount",
		Help:      "Number of requests recieved",
	}, fieldKeys)

	requestLatency := metrics.NewTimeHistogram(time.Microsecond, kitprometheus.NewSummary(stdprometheus.SummaryOpts{
		Namespace: "indexGroup",
		Subsystem: "VLAD",
		Name:      "requestLatencyMicroseconds",
		Help:      "Total duration of requests in microseconds.",
	}, fieldKeys))

	// Add custom instrumentation interfaces
	//
	//

	// Wire everything together
	var svc indexService
	svc = service{}
	svc = loggingMiddleware{logger, svc}

	// Add the custom instrumentation to the instrumentationMiddleware
	svc = instrumentationMiddleware{requestCount, requestLatency, svc}

	handleindex := httptransport.NewServer(
		ctx,
		makeindexEndpoint(svc),
		decodeindexRequest,
		encodeResponse,
	)

	http.Handle("/index", handleindex)
	http.Handle("/metrics", stdprometheus.Handler())
	_ = logger.Log("msg", "HTTP", "addr=", os.Getenv("U_INDEX_URL"))
	_ = logger.Log("err", http.ListenAndServe(fmt.Sprintf(":%s", os.Getenv("U_INDEX_PORT")), nil), nil)
}
